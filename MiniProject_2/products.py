import tkinter as tk
from tkinter import messagebox
from database import create_connection

BG="#f4f6f8"
WHITE="#ffffff"
BLUE="#2563eb"
DARK="#172033"
RED="#dc2626"

def product_window(parent):

    window=tk.Toplevel(parent)

    window.title("Products")
    window.state("zoomed")
    window.configure(bg=BG)


    tk.Label(
        window,
        text="📦 Product Management",
        font=("Arial",30,"bold"),
        fg=DARK,
        bg=BG
    ).pack(pady=25)


    form=tk.Frame(
        window,
        bg=WHITE,
        padx=35,
        pady=25
    )

    form.pack()


    tk.Label(
        form,
        text="Product Name",
        font=("Arial",11,"bold"),
        bg=WHITE
    ).grid(row=0,column=0,padx=10,pady=10)


    name=tk.Entry(
        form,
        width=30,
        font=("Arial",12)
    )

    name.grid(
        row=0,
        column=1,
        padx=10,
        pady=10,
        ipady=5
    )


    tk.Label(
        form,
        text="Price",
        font=("Arial",11,"bold"),
        bg=WHITE
    ).grid(row=1,column=0,padx=10,pady=10)


    price=tk.Entry(
        form,
        width=30,
        font=("Arial",12)
    )

    price.grid(
        row=1,
        column=1,
        padx=10,
        pady=10,
        ipady=5
    )


    tk.Label(
        form,
        text="Quantity",
        font=("Arial",11,"bold"),
        bg=WHITE
    ).grid(row=2,column=0,padx=10,pady=10)


    quantity=tk.Entry(
        form,
        width=30,
        font=("Arial",12)
    )

    quantity.grid(
        row=2,
        column=1,
        padx=10,
        pady=10,
        ipady=5
    )


    listbox=tk.Listbox(
        window,
        width=100,
        height=15,
        font=("Arial",12)
    )

    listbox.pack(pady=25)


    def load_products():

        listbox.delete(
            0,
            tk.END
        )

        cursor,con=create_connection()

        cursor.execute(
            "SELECT * FROM PRODUCTS"
        )

        products=cursor.fetchall()

        con.close()

        for p in products:

            listbox.insert(
                tk.END,
                f"ID: {p[0]} | {p[1]} | Price: ₹{p[2]} | Stock: {p[3]}"
            )


    def add_product():

        if name.get()=="" or price.get()=="" or quantity.get()=="":
            messagebox.showwarning(
                "Product",
                "Please fill all fields"
            )
            return

        try:

            cursor,con=create_connection()

            cursor.execute("""
            INSERT INTO PRODUCTS(PNAME,PRICE,QUANTITY)
            VALUES(?,?,?)
            """,(
                name.get(),
                float(price.get()),
                int(quantity.get())
            ))

            con.commit()
            con.close()

            messagebox.showinfo(
                "Product",
                "Product added successfully!"
            )

            name.delete(0,tk.END)
            price.delete(0,tk.END)
            quantity.delete(0,tk.END)

            load_products()

        except ValueError:

            messagebox.showerror(
                "Error",
                "Price and Quantity must be numbers"
            )


    def delete_product():

        selected=listbox.curselection()

        if not selected:

            messagebox.showwarning(
                "Delete",
                "Select a product first"
            )

            return

        text=listbox.get(
            selected[0]
        )

        pid=text.split("|")[0].replace(
            "ID:",
            ""
        ).strip()

        cursor,con=create_connection()

        cursor.execute(
            "DELETE FROM PRODUCTS WHERE PID=?",
            (pid,)
        )

        con.commit()
        con.close()

        messagebox.showinfo(
            "Product",
            "Product deleted!"
        )

        load_products()


    tk.Button(
        form,
        text="ADD PRODUCT",
        width=20,
        height=2,
        bg=BLUE,
        fg=WHITE,
        relief="flat",
        cursor="hand2",
        command=add_product
    ).grid(
        row=3,
        column=0,
        pady=15
    )


    tk.Button(
        form,
        text="DELETE PRODUCT",
        width=20,
        height=2,
        bg=RED,
        fg=WHITE,
        relief="flat",
        cursor="hand2",
        command=delete_product
    ).grid(
        row=3,
        column=1,
        pady=15
    )


    tk.Button(
        window,
        text="REFRESH",
        width=20,
        command=load_products
    ).pack()


    load_products()