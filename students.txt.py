
w=open("students.txt","w")
w.write("Vignesh_K-124005126-EEE \n"
     "Ram_shakthi_R_S-124005084-EEE \n"
     "Vittal_N-124158096-CS \n")
w.close()
s=open("students.txt","r")
stu=s.readlines()
s.close()
def readdet():
    r=open("students.txt","r")
    print(r.read())   
    r.close()
def insdet():
    app=input("enter student data to be added:")
    stu.append(app)
    print(stu)
def deldet():
    na=input("Enter name: ")
    k=0
    for i in stu:
        k+=1
        if na in i:
            stu.pop(k-1)
            break
    print(stu)
def inter():
    print("1.Read \n""2.insert\n""3.Remove\n")
    inp=input("enter your choice:")
    if inp=="1":
      readdet()
    elif inp=="2":
       insdet()
    elif inp=="3":
       deldet()
    else:
       exit()
inter()





          
          