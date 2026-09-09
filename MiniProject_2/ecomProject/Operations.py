import sqlite3
from passwordHashing import hash_pass
from database import connect_users_table

def create_connection():
    con=sqlite3.connect("ecomm.db")
    return con.cursor(),con

#<-----------------Add User (Insert)-------------->#
def add_user(uname,uemail,uphone,upass):
    try:
            cursor,con=create_connection()
            hashed_password=hash_pass(upass)
            connect_users_table()
            cursor.execute('''
                INSERT INTO USERS (UNAME, UEMAIL,UPHONE_NUMBER,UPASSWORD)
                VALUES (?,?,?,?) ''',(uname,uemail,uphone,hashed_password))
            print("Log 4:- Data Inserted") 
            con.commit()
            return True
    except sqlite3.IntegrityError:
        print(uemail,"Already Exists in the database")
        return False    
    finally:
        con.close()    
  
#<-----------------Delete Table--------------------->#
def delete_table():
    cursor,con=create_connection()
    cursor.execute('''
    DROP TABLE USERS;                   
                   ''') 
    con.commit()
    con.close()
#<----------------User Login----------------------->#
def user_login(email,password):
    hashed_password=hash_pass(password)
    
    cursor,con=create_connection()
    
    cursor.execute('''
    SELECT * FROM USERS 
    WHERE UEMAIL = ? AND
    UPASSWORD = ?''',(email,hashed_password))
    
    user=cursor.fetchone()
    
    if user!=None:
        print("Login is Sucessfull")
        print(email,"!!! Welcome to your account")
        return True
        
    else:
        print("Invalid Email or Password \n Try Again")
        return None
    con.close()
           
