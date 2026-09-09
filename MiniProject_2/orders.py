import tkinter as tk
from tkinter import messagebox
from database import create_connection
import auth
from cart import cart

def checkout_window(parent):

    if not cart:

        messagebox.showwarning(
            "Checkout",
            "Your cart is empty"
        )

        return


    total=sum(
        item[2]
        for item in cart
    )


    window=tk.Toplevel(parent)

    window.title(
        "Checkout"
    )

    window.geometry(
        "550x500"
    )

    window.configure(
        bg="#f4f6f8"
    )


    tk.Label(
        window,
        text="💳 Checkout",
        font=("Arial",28,"bold"),
        bg="#f4f6f8",
        fg="#172033"
    ).pack(pady=25)


    tk.Label(
        window,
        text="Order Summary",
        font=("Arial",18,"bold"),
        bg="#f4f6f8"
    ).pack(pady=10)


    box=tk.Listbox(
        window,
        width=55,
        height=10,
        font=("Arial",12)
    )

    box.pack(pady=15)


    for item in cart:

        box.insert(
            tk.END,
            f"{item[1]}     ₹{item[2]}"
        )


    tk.Label(
        window,
        text=f"Total Amount: ₹{total:.2f}",
        font=("Arial",20,"bold"),
        fg="#16a34a",
        bg="#f4f6f8"
    ).pack(pady=15)


    def place_order():

        cursor,con=create_connection()


        cursor.execute(
            """
            INSERT INTO ORDERS(UID,TOTAL)
            VALUES(?,?)
            """,
            (
                auth.current_user[0],
                total
            )
        )


        order_id=cursor.lastrowid


        for item in cart:

            cursor.execute(
                """
                INSERT INTO ORDER_ITEMS
                (OID,PID,QUANTITY,PRICE)
                VALUES(?,?,?,?)
                """,
                (
                    order_id,
                    item[0],
                    1,
                    item[2]
                )
            )


        con.commit()
        con.close()


        cart.clear()


        messagebox.showinfo(
            "Order",
            "🎉 Order placed successfully!"
        )


        window.destroy()


    tk.Button(
        window,
        text="PLACE ORDER",
        width=30,
        height=2,
        font=("Arial",12,"bold"),
        bg="#16a34a",
        fg="white",
        relief="flat",
        cursor="hand2",
        command=place_order
    ).pack(pady=20)