import csv
import pandas as pd
def fib(num):
  a=0
  b=1
  if num<0:
    print("incorrect input")
  elif num==0:
    return 0
  elif num==1:
    return 1
  else:
    for i in range(1,num):
      c=a+b
      a=b
      b=c
    return b
  
def fact(num):
  fact=1
  for i in range(1,num+1):
    fact=fact*i
  return fact
num=int(input("enter an integer:"))
diction={num:(fib(num),fact(num))}
print(diction)
header_list=["number","fibonacci value","factorial"]
c=open("factdic.csv","w",newline="")
wr=csv.writer(c)
for key in diction:
  list1=[key,diction[key][0],diction[key][1]]
  wr.writerow(list1)
c.close()
file=open("factdic.csv","r")
file.to_csv("factdic.csv",header=header_list,index=False)
print(file.read())
file.close()

    


