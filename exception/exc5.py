import csv
acc_no=["4576","2876","4236","4558"]
title=['fundamentals of power electronics','ikigai','atomic habits','millionare fastlane']
publisher=['penguin','tata mcgraw','sagar','oswal']
year=[2006,2014,2016,2019]
price=['655','500','389','455']
booklist=[acc_no,title,publisher,year,price]
with open("booklist.csv","w",newline="") as file:
    csv.writer(file).writerows(booklist)
    csv.writer(file).writerows([title])

  
