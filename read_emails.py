import imaplib
import email
def read_emails(user,password):
    def extract_body(payload):
        if isinstance(payload,str):
            return payload
        else:
            return '\n'.join([extract_body(part.get_payload()) for part in payload])

    conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    conn.login(user, password)
    conn.select()
    typ, data = conn.search(None, 'UNSEEN')
    emails = []
    try:
        for num in data[0].split():
            typ, msg_data = conn.fetch(num, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    subject=msg['subject']
                    #print(subject)
                    payload=msg.get_payload()
                    body=extract_body(payload)
                    emails.append(body)
            typ, response = conn.store(num, '+FLAGS', r'(\Seen)')
    finally:
        try:
            conn.close()
        except:
            pass
        conn.logout()
    a = emails
    a = [i[:i.find('\r\n')] for i in a]
    return a
