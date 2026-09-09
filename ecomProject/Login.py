import tkinter as tk
from tkinter import messagebox

from Operations import user_login
def Login():
    email=login_email.get()
    password=login_pass.get()
    if email=="" or password=="":
        messagebox.showwarning(title="Feilds cannot be empty")
    else:
        result=user_login(email,password)
        if result:
            messagebox.showinfo(title="Login Passed",message="Welcome to account")
        else:
            messagebox.showerror(title=":Login Failed",message="Invalid Credentials") 
    login_email.delete(0,30)
    login_pass.delete(0,30)
                                          
root=tk.Tk()
root.geometry("500x500")
root.title("User Login Page")

tk.Label(root,text="Login Page",font=("Arial",20)).pack(pady=20)

tk.Label(root,text="Enter Email ID",font=("Arial",15)).pack(pady=10)
login_email=tk.Entry(root,width=30)
login_email.pack(pady=10)

tk.Label(root,text="Enter Password",font=("Arial",15)).pack(pady=20)
login_pass=tk.Entry(root,width=30,show="*")
login_pass.pack(pady=10)

tk.Button(
    root,
    text="LOGIN",background="pink",
    command=Login
).pack(pady=20)

tk.mainloop()