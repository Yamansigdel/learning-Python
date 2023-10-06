import smtplib

conn=smtplib.SMTP('smtp.gmail.com', 587)

conn.ehlo()
conn.starttls()
password='' 
conn.login('yamansigdel999@gmail.com','password')
conn.sendmail('yamansigdel999@gmail.com','yamansigdel999@gmail.com','Subject: So long...\n\nDear Yum\n So long, and thanks for the fish!!\n\n - From Yaman')
conn.quit()
