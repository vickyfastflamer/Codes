try:
  operand1=int(input("enter the first operand:"))
  operand2=int(input("enter the second operand:"))
  op=input("enter the operation to be performed:")
  result=0

  if op=='+':
    result=operand1+operand2
    print("the sum of two numbers is :",result)
  elif op=='-':
    result=operand1-operand2
    print("the difference between two numbers is :",result)
  elif op=='*':
    result=operand1*operand2
    print("the product of two numbers is :",result)
  elif op=="/":
     result=operand1/operand2
     print("the quotient obtained is :",result)
  elif op=="%":
     result=operand1/operand2
     print("the quotient obtained is :",result)
  elif op=="//":
     result=operand1/operand2
     print("the quotient obtained is :",result)
  else:
     raise ArithmeticError
except ArithmeticError:
   print("please enter a valid operand")
except:
   print("please enter all the inputs correctly") 



