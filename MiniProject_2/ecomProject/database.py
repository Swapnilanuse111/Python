import sqlite3 

def connect_users_table():
    con=sqlite3.connect("ecomm.db")
    print("Log 1:- Database is connected")

    cursor=con.cursor() 
    print("Log 2:- Cursor Object created")

    #<---------------Table Creation--------------->#

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS USERS(
    UID INTEGER PRIMARY KEY AUTOINCREMENT,
    UNAME TEXT NOT NULL,
    UEMAIL TEXT UNIQUE NOT NULL,
    UPHONE_NUMBER TEXT NOT NULL,
    UPASSWORD TEXT NOT NULL  
        );                             
            ''')
    print("Log 3:- Table created/Accessed")
