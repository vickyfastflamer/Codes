import csv
regno=["4647","5216","5236","5899"]
name=["vignesh","ramesh","venkatesh","suresh"]
marks1=[45,56,55,59]
marks2=[35,57,50,46]
marks3=[41,44,56,47]
students=[regno,name,marks1,marks2,marks3]
for i in range(len(marks1)):
    marks=(marks1[i]+marks2[i]+marks3[i])/3
with open("marks.csv","w") as p:
    wr=csv.writer(p)
    wr.writerows(students)
with open("marks.csv")as fp:
    obj=csv.reader(fp)
    for r in obj:
        tot=int(r[2])+int(r[3])+int(r[4])
        avg=tot/3
        r.append(tot)
        r.append(avg)
        print(r)



