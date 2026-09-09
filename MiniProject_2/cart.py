import tkinter as tk
from tkinter import messagebox
from database import create_connection

cart=[]

BG="#f4f6f8"
WHITE="#ffffff"
BLUE="#2563eb"
GREEN="#16a34a"
DARK="#172033"

def cart_window(parent):

    window=tk.Toplevel(parent)

    window.title("Shopping Cart")
    window.state("zoomed")
    window.configure(bg=BG)


    tk.Label(
        window,
        text="🛍️ Shopping Cart",
        font=("Arial",30,"bold"),
        fg=DARK,
        bg=BG
    ).pack(pady=25)


    listbox=tk.Listbox(
        window,
        width=100,
        height=18,
        font=("Arial",12)
    )

    listbox.pack(pady=20)


    def load_products():

        listbox.delete(
            0,
            tk.END
        )

        cursor,con=create_connection()

        cursor.execute(
            "SELECT * FROM PRODUCTS WHERE QUANTITY>0"
        )

        products=cursor.fetchall()

        con.close()

        for p in products:

            listbox.insert(
                tk.END,
                f"ID: {p[0]} | {p[1]} | ₹{p[2]} | Stock: {p[3]}"
            )


    def add_to_cart():

        selected=listbox.curselection()

        if not selected:

            messagebox.showwarning(
                "Cart",
                "Select a product"
            )

            return


        text=listbox.get(
            selected[0]
        )

        parts=text.split("|")

        pid=int(
            parts[0].replace(
                "ID:",
                ""
            ).strip()
        )

        name=parts[1].strip()

        price=float(
            parts[2].replace(
                "₹",
                ""
            ).strip()
        )


        cart.append(
            (pid,name,price)
        )


        messagebox.showinfo(
            "Cart",
            f"{name} added to cart!"
        )


    def view_cart():

        cart_window2=tk.Toplevel(
            window
        )

        cart_window2.title(
            "My Cart"
        )

        cart_window2.geometry(
            "650x550"
        )

        cart_window2.configure(
            bg=BG
        )


        tk.Label(
            cart_window2,
            text="🛒 My Cart",
            font=("Arial",24,"bold"),
            bg=BG,
            fg=DARK
        ).pack(pady=20)


        box=tk.Listbox(
            cart_window2,
            width=70,
            height=15,
            font=("Arial",12)
        )

        box.pack(pady=15)


        total=0


        for item in cart:

            box.insert(
                tk.END,
                f"{item[1]} - ₹{item[2]}"
            )

            total+=item[2]


        tk.Label(
            cart_window2,
            text=f"Total: ₹{total:.2f}",
            font=("Arial",20,"bold"),
            bg=BG,
            fg=GREEN
        ).pack(pady=15)


    tk.Button(
        window,
        text="ADD TO CART",
        width=25,
        height=2,
        bg=BLUE,
        fg=WHITE,
        relief="flat",
        cursor="hand2",
        command=add_to_cart
    ).pack(pady=10)


    tk.Button(
        window,
        text="VIEW CART",
        width=25,
        height=2,
        bg=GREEN,
        fg=WHITE,
        relief="flat",
        cursor="hand2",
        command=view_cart
    ).pack(pady=10)


    load_products()