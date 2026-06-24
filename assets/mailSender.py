import os
import smtplib
import sys
from email.message import EmailMessage


def send_mail_with_attachment(emails, zipped_file_path, file_name):
    
    emails = emails if len(emails) > 0 else ['to@mail.com', 'to@mail2.com']
    content = """\
        Bonjour!

        La liste des revenues part sociétés

        --Edouard
        """ 
  
    msg = EmailMessage()
    msg.set_content(content)
        
    msg['Subject'] = f'Company income list "company_report.zip"'
    msg['From'] = 'my@mail.com'
    msg['To'] = ', '.join(emails)
    
    with open(zipped_file_path, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(zipped_file_path)

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="octet-stream",
        filename=file_name
    )

    
    # email server
    server = smtplib.SMTP('localhost:2525')
    server.send_message(msg)
    server.quit() 
    
    sys.exit(0)
       