import random
randpin=random.randint(0,1000000)
print(randpin)


def otpauth(randpin):
  pin=input("enter the otp here:")
  if (pin == str(randpin)):
    print("you are successfully authenticated")
  else:
    print("please check your otp")


otpauth(randpin)