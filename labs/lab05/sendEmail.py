import smtplib
from email.mime.text import MIMEText

msg = MIMEText("The body of the email is here")

msg['Subject'] = "An Email Alert"
msg['From'] = "student@gmail.com"
msg['To'] = "webmaster@gmail.com"

s = smtplib.SMTP('localhost')
# s = smtplib.SMTP('smtp.gmail.com', 587)
# s.starttls()
s.login('somemail@gmail.com', 'somepass')
s.send_message(msg)
s.quit()