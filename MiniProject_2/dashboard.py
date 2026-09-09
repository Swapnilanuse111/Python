import tkinter as tk
import auth
from products import product_window
from cart import cart_window
from orders import checkout_window

BG="#f4f6f8"
WHITE="#ffffff"
BLUE="#2563eb"
DARK="#172033"
GRAY="#64748b"
GREEN="#16a34a"
ORANGE="#f59e0b"

def dashboard_window(root,logout):

    window=tk.Toplevel(root)

    window.title("E-Commerce Dashboard")
    window.state("zoomed")
    window.configure(bg=BG)

    name=auth.current_user[1]


    # ---------------- HEADER ----------------

    header=tk.Frame(
        window,
        bg=WHITE,
        height=80
    )

    header.pack(
        fill="x"
    )

    tk.Label(
        header,
        text="🛒 ShopEasy",
        font=("Arial",24,"bold"),
        fg=BLUE,
        bg=WHITE
    ).pack(
        side="left",
        padx=35,
        pady=20
    )


    tk.Label(
        header,
        text=f"Hello, {name} 👋",
        font=("Arial",14,"bold"),
        fg=DARK,
        bg=WHITE
    ).pack(
        side="right",
        padx=35
    )


    # ---------------- WELCOME ----------------

    tk.Label(
        window,
        text="Welcome to your Dashboard",
        font=("Arial",32,"bold"),
        fg=DARK,
        bg=BG
    ).pack(pady=(45,5))


    tk.Label(
        window,
        text="Manage products, shopping cart and orders",
        font=("Arial",13),
        fg=GRAY,
        bg=BG
    ).pack()


    # ---------------- CARDS ----------------

    cards=tk.Frame(
        window,
        bg=BG
    )

    cards.pack(
        pady=45
    )


    # PRODUCT CARD

    product_card=tk.Frame(
        cards,
        bg=WHITE,
        width=250,
        height=180
    )

    product_card.grid(
        row=0,
        column=0,
        padx=15
    )

    product_card.pack_propagate(False)


    tk.Label(
        product_card,
        text="📦",
        font=("Arial",35),
        bg=WHITE
    ).pack(pady=(20,5))


    tk.Label(
        product_card,
        text="Products",
        font=("Arial",18,"bold"),
        fg=DARK,
        bg=WHITE
    ).pack()


    tk.Button(
        product_card,
        text="OPEN",
        width=18,
        bg=BLUE,
        fg=WHITE,
        relief="flat",
        cursor="hand2",
        command=lambda:product_window(window)
    ).pack(pady=10)


    # CART CARD

    cart_card=tk.Frame(
        cards,
        bg=WHITE,
        width=250,
        height=180
    )

    cart_card.grid(
        row=0,
        column=1,
        padx=15
    )

    cart_card.pack_propagate(False)


    tk.Label(
        cart_card,
        text="🛍️",
        font=("Arial",35),
        bg=WHITE
    ).pack(pady=(20,5))


    tk.Label(
        cart_card,
        text="Shopping Cart",
        font=("Arial",18,"bold"),
        fg=DARK,
        bg=WHITE
    ).pack()


    tk.Button(
        cart_card,
        text="OPEN",
        width=18,
        bg=GREEN,
        fg=WHITE,
        relief="flat",
        cursor="hand2",
        command=lambda:cart_window(window)
    ).pack(pady=10)


    # CHECKOUT CARD

    checkout_card=tk.Frame(
        cards,
        bg=WHITE,
        width=250,
        height=180
    )

    checkout_card.grid(
        row=0,
        column=2,
        padx=15
    )

    checkout_card.pack_propagate(False)


    tk.Label(
        checkout_card,
        text="💳",
        font=("Arial",35),
        bg=WHITE
    ).pack(pady=(20,5))


    tk.Label(
        checkout_card,
        text="Checkout",
        font=("Arial",18,"bold"),
        fg=DARK,
        bg=WHITE
    ).pack()


    tk.Button(
        checkout_card,
        text="OPEN",
        width=18,
        bg=ORANGE,
        fg=WHITE,
        relief="flat",
        cursor="hand2",
        command=lambda:checkout_window(window)
    ).pack(pady=10)


    # ---------------- LOGOUT ----------------

    tk.Button(
        window,
        text="LOGOUT",
        font=("Arial",12,"bold"),
        width=25,
        height=2,
        bg="#dc2626",
        fg=WHITE,
        relief="flat",
        cursor="hand2",
        command=lambda:[
            window.destroy(),
            logout()
        ]
    ).pack(pady=20)


    # ---------------- FOOTER ----------------

    tk.Label(
        window,
        text="ShopEasy © 2026 | Python + Tkinter + SQLite",
        font=("Arial",10),
        fg=GRAY,
        bg=BG
    ).pack(
        side="bottom",
        pady=20
    )