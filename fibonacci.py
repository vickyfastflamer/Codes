#function define pandrom
def fib(num):
  a=0
  b=1
  if num<0:
    print("incorrect input")
  elif num==0:
    return 0
  elif num==1:
    print(b)
  else:
    for i in range(1,num):
      print(b)
      c=a+b
      a=b
      b=c
    return b
    

print(fib(5))



