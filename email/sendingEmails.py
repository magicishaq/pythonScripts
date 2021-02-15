import smtplib #simple mail transfer protocol mod

conn = smtplib.SMTP('smtp.gmail.com', 587)
#connet to the server
conn.ehlo() # to start the connection

conn.starttls() #sends password to be encrypted

conn.login('emailAccount', 'password')
email = '''Subject: So long...
thanks for all the fish'''
conn.sendmail('ishaqkhan1993@gmail.com' , email) 

conn.quit()

