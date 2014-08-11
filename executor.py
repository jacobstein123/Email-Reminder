#-------------------------------------------------------------------------------
# Name:        email reminder
# Purpose:     email reminder system
#
# Author:      Jacob Stein
#
# Created:     08/08/2013
# Copyright:   (c) Jacob Stein 2013
#-------------------------------------------------------------------------------

from read_emails import read_emails
import datetime
from gmail import send_email

class Reminder:
    def __init__(self,address="",message="",date=(0,0,0),time=(0,0)):
        self.address = address
        self.message = message
        self.date = date
        self.time = time
    def get_address(self):
        return self.address
    def get_message(self):
        return self.message
    def get_date(self):
        return self.date
    def get_time(self):
        return self.time
    def __str__(self):
        return "Address: {address}, Message: {message}, Date: {date}, Time: {time}".format(address=self.address,message=self.message,date=self.date,time=self.time)

def get_new_reminders(user,password):
    new_reminders = []
    emails = read_emails(user,password)
    for email in emails:
        reminder = email.split(',')
        address = reminder[0]
        message = reminder[1]
        date = [int(i) for i in reminder[2].split('.')] #(month,day,year)
        time = [int(i) for i in reminder[3].split('.')] #(hour,minute)
        new_reminders.append(Reminder(address,message,date,time))
    return new_reminders

def get_due_reminders(reminders):
    due_reminders = []
    now = datetime.datetime.now()
    for reminder in reminders:
        print str(reminder)
        if reminder.date == [now.month,now.day,now.year]:
            if (reminder.time[0] < now.hour) or (reminder.time[0] == now.hour and reminder.time[1] <= now.minute): #if the hour has passed, or if it is the right hour and the minute has passed
                due_reminders.append(reminder)
    return due_reminders

def send_reminders(due_reminders,email,password):
    for reminder in due_reminders:
        send_email(email,password,reminder.address,reminder.message,"Your email reminder has arrived!")


def main():
    reminders = []
    email ='user'
    password = 'pass'
    while True:
        reminders += get_new_reminders(email,password)
        for reminder in reminders:
            print reminder.message,reminder.address,reminder.date,reminder.time
        due_reminders = get_due_reminders(reminders)
        send_reminders(due_reminders,email,password)
        reminders = [i for i in reminders if i not in due_reminders]
        due_reminders = []


if __name__ == '__main__':
    main()
