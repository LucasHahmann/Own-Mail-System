from email.message import EmailMessage
import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import json

def checkLogin(username, password):
    imap = imaplib.IMAP4_SSL("imap.1blu.de")
    try:
        imap.login(username, password)
        return True
    except:
        return False

def write_json(new_data, filename='mail.json'):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        print(file_data)
        # Join new_data with file_data inside emp_details
        file_data[0]["mails"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)


def getMails(username, password):
    os.remove("mail.json")
    with open('mail.json', 'w') as outfile:
        outfile.write('[{"mails": []}]')
    # create an IMAP4 class with SSL 
    imap = imaplib.IMAP4_SSL("imap.1blu.de")
    # authenticate
    imap.login(username, password)
    status, messages = imap.select("INBOX")
    # total number of emails
    messages = int(messages[0])
    # number of top emails to fetch
    N = messages
    for i in range(messages, messages-N, -1):
    #for i in (1, messages):
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    # if it's a bytes, decode to str
                    subject = subject.decode(encoding)
                # decode email sender
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes):
                    From = From.decode(encoding)
                # if the email message is multipart
                if msg.is_multipart():
                    # iterate over email parts
                    for part in msg.walk():
                        # extract content type of email
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            # get the email body
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            # print text/plain emails and skip attachments
                            mail= {"ID": i,"From": From,"Subject": subject,"Body": body}
                            write_json(mail)
                else:
                    # extract content type of email
                    content_type = msg.get_content_type()
                    # get the email body
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        # print only text email parts
                        mail= {"ID": i,"From": From,"Subject": subject,"Body": body}
                        write_json(mail)
                        

    imap.close()
    imap.logout()