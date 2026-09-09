import tkinter as tk
import database
from auth import login_window,registration_window
from dashboard import dashboard_window

BG="#f4f6f8"
WHITE="#ffffff"
BLUE="#2563eb"
DARK="#172033"
GRAY="#64748b"

root=tk.Tk()

root.title(
    "ShopEasy - E-Commerce Application"
)

root.state(
    "zoomed"
)

root.configure(
    bg=BG
)


def open_login():

    login_window(
        root,
        open_dashboard,
        open_registration
    )


def open_registration():

    registration_window(
        root,
        open_login
    )


def open_dashboard():

    dashboard_window(
        root,
        open_login
    )


# ---------------- HOME PAGE ----------------

tk.Label(
    root,
    text="🛒",
    font=("Arial",60),
    bg=BG
).pack(
    pady=(100,10)
)


tk.Label(
    root,
    text="ShopEasy",
    font=("Arial",45,"bold"),
    fg=BLUE,
    bg=BG
).pack()


tk.Label(
    root,
    text="Simple Python E-Commerce Application",
    font=("Arial",18),
    fg=GRAY,
    bg=BG
).pack(
    pady=10
)


tk.Label(
    root,
    text="Python  •  Tkinter  •  SQLite",
    font=("Arial",12),
    fg=GRAY,
    bg=BG
).pack(
    pady=5
)


button_frame=tk.Frame(
    root,
    bg=BG
)

button_frame.pack(
    pady=40
)


tk.Button(
    button_frame,
    text="LOGIN",
    width=25,
    height=2,
    font=("Arial",13,"bold"),
    bg=BLUE,
    fg=WHITE,
    relief="flat",
    cursor="hand2",
    command=open_login
).grid(
    row=0,
    column=0,
    padx=15
)


tk.Button(
    button_frame,
    text="CREATE ACCOUNT",
    width=25,
    height=2,
    font=("Arial",13,"bold"),
    bg=WHITE,
    fg=BLUE,
    relief="solid",
    bd=1,
    cursor="hand2",
    command=open_registration
).grid(
    row=0,
    column=1,
    padx=15
)


tk.Label(
    root,
    text="© 2026 ShopEasy | E-Commerce Learning Project",
    font=("Arial",10),
    fg=GRAY,
    bg=BG
).pack(
    side="bottom",
    pady=25
)


root.mainloop()