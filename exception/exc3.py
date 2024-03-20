input_=[]
n=int(input("enter the number of lines:"))
for i in range(n):
        x=input()
        if(x=='end'):
                break
        else:
              input_.append(x)

with open("file.txt","w") as np:
        for p in input_:
                np.write(p)
for n in open('file.txt'):
    print('input given is:',n)
        
        