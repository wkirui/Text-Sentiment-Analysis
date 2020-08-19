# email final results
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# get mail server settings
from settings import mail_username,mail_password,mail_recipient,mail_sender

# import final results dataframe
from process_tweets import top_20_comment_results

msg = MIMEMultipart()
msg['From'] = mail_sender
msg['To'] = mail_recipient
msg['Subject'] = 'Text Sentiment Analysis Report'
message = 'Here are the final results from the analysis'

# create html message
html_message = """\
    <html>
        <head></head>
        <body>
        {0}
        </body>
    </html>
""".format(top_20_comment_results.to_html)
# attach message
msg.attach(MIMEText(message))
msg.attach(MIMEText(html_message))

mailserver = smtplib.SMTP(host='smtp.gmail.com',port=587)

mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login(mail_username, mail_password)

mailserver.sendmail(mail_sender,mail_recipient,msg.as_string())

mailserver.quit()