


from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import re

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465

SMTP_USER = 'YOUR_EMAIL'
SMTP_PASSWORD = 'PASSWORD'



class Email():
	def __init__(self):
		self.from_email = SMTP_USER
		self.subj_layout = 'Hello, world'
		self.cont_layout = '''This is auto forwadrding email...'''



	def send_mail(self, name, addr, attachment = None, contents=None):


		msg = MIMEMultipart('alternative') 


		if attachment: 
			msg = MIMEMultipart('mixed')


		msg['From'] = self.from_email
		msg['To'] = addr
		msg['Subject'] = name + self.subj_layout

		if not contents:
			contents = name + self.cont_layout



		text = MIMEText(_text=contents)
		msg.attach(text) 



		if attachment:
			from email.mime.base import MIMEBase
			from email import encoders


			file_data = MIMEBase('application', 'octect-stream')
			file_data.set_payload(open(attachment, 'rb').read())
			encoders.encode_base64(file_data)

			import os
			filename = os.path.basename(attachment)

			file_data.add_header('Content-Disposition', 'attachment; filename="' + filename + '"')

			msg.attach(file_data)



		smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) 
		smtp.login(SMTP_USER, SMTP_PASSWORD)
		smtp.sendmail(SMTP_USER, addr, msg.as_string())
		smtp.close()

if __name__ == '__main__':
	e = Email()
	e.send_mail('RECIPIENNT_NAME', 'RECIPIENNT_EMAIL')








