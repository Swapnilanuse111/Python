import sqlite3
def create_connection():
    # Database connection
    con = sqlite3.connect("ecomm.db") #Here If The DB Is Not Present inside the database it will automaticallly created in our sqlite3
    #If The DB Is Created Then It Will Only Connect To the DrataBase 
    print("Log1: Database Connection Created")
    # Cursor creation---it userd To Create Table,update and Add some data ainside the database    
    cursor = con.cursor()
    print("Log2: Cursor Created")
    # Create USERS table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS USERS(
            UID INTEGER PRIMARY KEY AUTOINCREMENT,
            UNAME TEXT NOT NULL,
            UEMAIL TEXT UNIQUE NOT NULL,
            UPASSWORD TEXT NOT NULL
        )
    """)
    con.commit()
    print("Log3: USERS Table Created")
    return cursor, con