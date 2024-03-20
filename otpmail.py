import random
import smtplib
from auth import auth
smtp_server="smtp.gmail.com"
port='587'
send_mail="124005126@sastra.ac.in"
send_pass="kvskv0307"
receiver_mail=input("SEND TO:")
randpin=random.randint(0,1000000)
message=("Hello user this is a OTP from our organization.. "+ str(randpin))
server=smtplib.SMTP(smtp_server,port)
server.starttls()
server.login(send_mail,send_pass)
server.sendmail(send_mail,receiver_mail,message)
def otpauth(randpin):
  pin=input("enter the otp here:")
  if (pin == str(randpin)):
    print("you are successfully authenticated")
  else:
    print("please check your otp")

otpauth(randpin)