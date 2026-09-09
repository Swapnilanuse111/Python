import tkinter as tk 
from tkinter import messagebox
from Operations import add_user

def Register():
    uemail=email.get()
    uname=name.get()
    uphone=ph_num.get()
    upass=password.get()
    
    if uemail=="" or uname=="" or uphone=="" or upass=="":
        messagebox.showerror(title="Empty Fields",message="All fields are mandatory")
    else:
        result=add_user(uname,uemail,uphone,upass)
        if result==True:
            messagebox.showinfo(title="Account Created",message="User has been created")
        else:
            messagebox.showerror(title="Registration Failed",message="Email Id already exists") 
    
    email.delete(0,30)
    name.delete(0,30)
    ph_num.delete(0,30)
    password.delete(0,30)           

root=tk.Tk()
root.geometry("1500x1000")
root.title("Ecomm Application")

tk.Label(root,text="Welcome to Ecomm Application",font=("Arial",25)).pack(pady=20)
tk.Label(root,text="Register Form",font=("Sans-serif",15)).pack(pady=15)

tk.Label(root,text="Enter Email:-",font=("Sans-serif",15)).pack()
email=tk.Entry(root,width=30)
email.pack()

tk.Label(root,text="Enter Name:- ",font=("Sans-serif",15)).pack(pady=10)
name=tk.Entry(root,width=30)
name.pack()

tk.Label(root,text="Enter Phone Number:- ",font=("Sans-serif",15)).pack(pady=10)
ph_num=tk.Entry(root,width=30)
ph_num.pack()

tk.Label(root,text="Enter Password:- ",font=("Sans-serif",15)).pack(pady=10)
password=tk.Entry(root,width=30,show="*")
password.pack()

tk.Button(
    root,
    text="SUBMIT",
    command=Register
).pack(pady=10)





root.mainloop()
