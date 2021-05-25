import smtplib
import getpass
from email.mime.text import MIMEText


def send_email():
    sender_address = 'sumitkumarsinghd2002@gmail.com'
    password =getpass.getpass()
    subject = 'AI Mafia - machine learning'
    msg = '''
      Learn.Inspire.Grow!
    '''

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_address,password)

    # draft my message body
    msg=MIMEText(msg)
    msg['subject'] = subject
    msg['from'] = sender_address
    msg['to'] = 'sumitkumarsinghd2002@gmail.com'
    recipients = 'sumitkumarsinghd2002@gmail.com'
    server.sendmail(sender_address,recipients,msg.as_string())

send_email()
