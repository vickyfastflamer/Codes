try:
    filename=input("enter the filename to be searched:")
    with open(filename,'r') as f:
       print(f.read())
    fp=open(filename,'r')
    print(fp.readlines())
    fpp=open(filename,'r')
    line=fpp.readline()
    while line:
           print(line)  
           line=fpp.readline()

except:
    print("enter a valid file name:::")