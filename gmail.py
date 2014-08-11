import smtplib
def send_email(email, password, recipient, body = '', subject = ''):
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.login(email, password)

    headers = "\r\n".join(["from: " + email,
                           "subject: " + subject,
                           "to: " + recipient,
                           "mime-version: 1.0",
                           "content-type: text/html"])

    # body_of_email can be plaintext or html!
    content = headers + "\r\n\r\n" + body
    session.sendmail(email, recipient, content)