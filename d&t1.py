from datetime import datetime,timedelta
print(" The invoice Due date program")
invdate=input("enter the date specified in invoice:(MM/DD/YY) ")
invoice_date=datetime.strptime(invdate,"%m/%d/%y")
print("invoice date:",invoice_date.strftime("%B %d, %Y"))
d_date=invoice_date + timedelta(days=30)
print("Due Date:",d_date.strftime("%B %d, %Y"))
c_date=datetime.now()
current_date=datetime.strftime(c_date,"%B %d,%Y")
print("Current Date:",current_date)
overdue=(c_date - d_date).days

if(overdue<=0):
    print("Thank you , there is no overdue;")
else:
    print("your bill is overdue by",overdue,"days")





