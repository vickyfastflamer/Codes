import smtplib
smtp_server="smtp.gmail.com"
port='587'
send_mail="124005126@sastra.ac.in"
send_pass=input("PASSWORD:")
receiver_mail=input("SEND TO:")
messsage=("Hi vicky fast flamer this is a OTP from your organization.. ")
server=smtplib.SMTP(smtp_server,port)
server.starttls()
server.login(send_mail,send_pass)
server.sendmail(send_mail,receiver_mail,messsage)