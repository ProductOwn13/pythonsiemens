import smtplib;
import ssl;
from email.mime.multipart import  MIMEMultipart;

s = smtplib.SMTP(host="mail.vinsys.com", port=587);
s.starttls()
s.login("nilesh.devdas@vinsys.com", "admin@1234");
msg = MIMEMultipart()
msg['From']='nilesh.devdas@vinsys.com'
msg['To'] = 'nilesh.devdas@outlook.com'
msg['Subject'] = "Thank you python"
s.send_message(msg)
s.close();
