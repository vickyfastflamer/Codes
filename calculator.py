num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
operation=(input("enter the operation to be done:"))
result=0
if operation=='+':
    result=num1+num2
    print("the sum of two numbers is ",result)
elif operation=='-':
    result=num1-num2
    print("the difference of two numbers is ",result)
elif operation=='*':
    result=num1*num2
    print("the product of two numbers is ",result)
elif operation=='/':
    result=num1/num2
    print("the result obtained from division of two numbers is ",result)

