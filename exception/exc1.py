#finding the factorial of the given number
num= int(input("enter the number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i

    
try:
    if(num<=20 and num>0):
       print("the factorial of the given number is :",fact)
    else:
        raise ValueError
except:
    print("please enter a positive number less than 20")



