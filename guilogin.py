from tkinter import *


USER=['124005126','124005016','124005161']
password='bank'
root=Tk()
root.title("Locker Access System")
root.geometry("1024x600")

def click():
    user=e1.get()
    passw=e2.get()
    for i in range(len(USER)):
      if user == USER[i] and passw == password : 
            msg.config(text="Good!", fg="green")
            import guic
            break
      else:
            # Display an error message
            msg.config(text="Please check your username or password", fg="red")
            # Continue to the next iteration
            continue

mylabel1=Label(root,text="Welcome to Locker access system")
mylabel1.pack()
eq1=Label(root,text="USERNAME:")
eq1.pack()
e1=Entry(root)
e1.pack()
eq2=Label(root,text="PASSWORD:")
eq2.pack()
e2=Entry(root,show="*")
e2.pack()
search=Button(root,text="Login",command=click)
search.pack()

msg = Message(root, width=200)
msg.pack()

root.mainloop()