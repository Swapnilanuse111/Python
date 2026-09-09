import sqlite3

DB_NAME="ABC.db"

def create_connection():
    con=sqlite3.connect(DB_NAME)
    cursor=con.cursor()
    return cursor,con

def create_tables():
    cursor,con=create_connection()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS USERS(
        UID INTEGER PRIMARY KEY AUTOINCREMENT,
        UNAME TEXT NOT NULL,
        UEMAIL TEXT UNIQUE NOT NULL,
        UPASSWORD TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS PRODUCTS(
        PID INTEGER PRIMARY KEY AUTOINCREMENT,
        PNAME TEXT NOT NULL,
        PRICE REAL NOT NULL,
        QUANTITY INTEGER NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ORDERS(
        OID INTEGER PRIMARY KEY AUTOINCREMENT,
        UID INTEGER NOT NULL,
        TOTAL REAL NOT NULL,
        ORDER_DATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ORDER_ITEMS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        OID INTEGER NOT NULL,
        PID INTEGER NOT NULL,
        QUANTITY INTEGER NOT NULL,
        PRICE REAL NOT NULL
    )
    """)

    con.commit()
    con.close()

create_tables()