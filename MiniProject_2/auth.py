import tkinter as tk
from tkinter import messagebox
import sqlite3
from database import create_connection
from HashPassword import hash_pass

current_user=None

BG="#f4f6f8"
WHITE="#ffffff"
BLUE="#2563eb"
DARK="#172033"
GRAY="#64748b"
GREEN="#16a34a"

def register_user(uname,uemail,upass):

    if uname=="" or uemail=="" or upass=="":
        messagebox.showwarning("Registration","Please fill all fields")
        return False

    hashed_password=hash_pass(upass)

    cursor,con=create_connection()

    try:
        cursor.execute("""
        INSERT INTO USERS(UNAME,UEMAIL,UPASSWORD)
        VALUES(?,?,?)
        """,(uname,uemail,hashed_password))

        con.commit()

        messagebox.showinfo(
            "Registration",
            "Account created successfully!"
        )

        return True

    except sqlite3.IntegrityError:
        messagebox.showerror(
            "Registration",
            "Email already exists!"
        )
        return False

    finally:
        con.close()


def login_user(email,password):

    global current_user

    if email=="" or password=="":
        messagebox.showwarning(
            "Login",
            "Please enter email and password"
        )
        return False

    hashed_password=hash_pass(password)

    cursor,con=create_connection()

    cursor.execute("""
    SELECT UID,UNAME,UEMAIL
    FROM USERS
    WHERE UEMAIL=? AND UPASSWORD=?
    """,(email,hashed_password))

    user=cursor.fetchone()

    con.close()

    if user:
        current_user=user
        return True

    messagebox.showerror(
        "Login Failed",
        "Invalid email or password"
    )

    return False


def registration_window(root,open_login):

    window=tk.Toplevel(root)

    window.title("Create Account")
    window.state("zoomed")
    window.configure(bg=BG)

    window.transient(root)

    card=tk.Frame(
        window,
        bg=WHITE,
        padx=60,
        pady=40
    )

    card.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

    tk.Label(
        card,
        text="🛒",
        font=("Arial",40),
        bg=WHITE
    ).pack()

    tk.Label(
        card,
        text="Create Account",
        font=("Arial",28,"bold"),
        fg=DARK,
        bg=WHITE
    ).pack(pady=5)

    tk.Label(
        card,
        text="Join our shopping application",
        font=("Arial",11),
        fg=GRAY,
        bg=WHITE
    ).pack(pady=(0,25))


    tk.Label(
        card,
        text="User Name",
        font=("Arial",11,"bold"),
        fg=DARK,
        bg=WHITE
    ).pack(anchor="w")

    name=tk.Entry(
        card,
        width=38,
        font=("Arial",13),
        relief="solid",
        bd=1
    )

    name.pack(
        pady=(5,15),
        ipady=8
    )


    tk.Label(
        card,
        text="Email",
        font=("Arial",11,"bold"),
        fg=DARK,
        bg=WHITE
    ).pack(anchor="w")

    email=tk.Entry(
        card,
        width=38,
        font=("Arial",13),
        relief="solid",
        bd=1
    )

    email.pack(
        pady=(5,15),
        ipady=8
    )


    tk.Label(
        card,
        text="Password",
        font=("Arial",11,"bold"),
        fg=DARK,
        bg=WHITE
    ).pack(anchor="w")

    password=tk.Entry(
        card,
        width=38,
        font=("Arial",13),
        show="*",
        relief="solid",
        bd=1
    )

    password.pack(
        pady=(5,20),
        ipady=8
    )


    def register():

        result=register_user(
            name.get(),
            email.get(),
            password.get()
        )

        if result:

            window.destroy()

            open_login()


    tk.Button(
        card,
        text="CREATE ACCOUNT",
        font=("Arial",12,"bold"),
        bg=BLUE,
        fg=WHITE,
        activebackground=BLUE,
        activeforeground=WHITE,
        width=32,
        height=2,
        relief="flat",
        cursor="hand2",
        command=register
    ).pack(pady=10)


    tk.Button(
        card,
        text="← Back to Login",
        font=("Arial",11),
        bg=WHITE,
        fg=BLUE,
        relief="flat",
        cursor="hand2",
        command=lambda:[
            window.destroy(),
            open_login()
        ]
    ).pack()


def login_window(root,open_dashboard,open_registration):

    window=tk.Toplevel(root)

    window.title("Login")
    window.state("zoomed")
    window.configure(bg=BG)

    window.transient(root)

    card=tk.Frame(
        window,
        bg=WHITE,
        padx=60,
        pady=45
    )

    card.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )


    tk.Label(
        card,
        text="🛍️",
        font=("Arial",40),
        bg=WHITE
    ).pack()


    tk.Label(
        card,
        text="Welcome Back",
        font=("Arial",28,"bold"),
        fg=DARK,
        bg=WHITE
    ).pack(pady=5)


    tk.Label(
        card,
        text="Login to continue shopping",
        font=("Arial",11),
        fg=GRAY,
        bg=WHITE
    ).pack(pady=(0,25))


    tk.Label(
        card,
        text="Email",
        font=("Arial",11,"bold"),
        fg=DARK,
        bg=WHITE
    ).pack(anchor="w")


    email=tk.Entry(
        card,
        width=38,
        font=("Arial",13),
        relief="solid",
        bd=1
    )

    email.pack(
        pady=(5,15),
        ipady=8
    )


    tk.Label(
        card,
        text="Password",
        font=("Arial",11,"bold"),
        fg=DARK,
        bg=WHITE
    ).pack(anchor="w")


    password=tk.Entry(
        card,
        width=38,
        font=("Arial",13),
        show="*",
        relief="solid",
        bd=1
    )

    password.pack(
        pady=(5,20),
        ipady=8
    )


    def login():

        if login_user(
            email.get(),
            password.get()
        ):

            window.destroy()

            open_dashboard()


    tk.Button(
        card,
        text="LOGIN",
        font=("Arial",12,"bold"),
        bg=BLUE,
        fg=WHITE,
        activebackground=BLUE,
        activeforeground=WHITE,
        width=32,
        height=2,
        relief="flat",
        cursor="hand2",
        command=login
    ).pack(pady=10)


    tk.Button(
        card,
        text="Create New Account",
        font=("Arial",11),
        bg=WHITE,
        fg=BLUE,
        relief="flat",
        cursor="hand2",
        command=lambda:[
            window.destroy(),
            open_registration()
        ]
    ).pack()