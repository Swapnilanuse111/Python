from database import create_connection
from HashPassword import hash_pass
# -----------------------------------------
# User Registration
# -----------------------------------------
def User_registration():
    print("\n--------- USER REGISTRATION ---------")
    uname = input("Enter User Name: ")
    uemail = input("Enter User Email: ")
    upass = input("Enter User Password: ")
    # Convert password into hash
    hashed_password = hash_pass(upass)
    # Create database connection
    cursor, con = create_connection()
    cursor.execute(
        """
        INSERT INTO USERS(UNAME, UEMAIL, UPASSWORD)
        VALUES(?,?,?)
        """,
        (uname, uemail, hashed_password)
    )
    con.commit()
    print("Registration Successful")
    con.close()
# -----------------------------------------
# User Login
# -----------------------------------------
def User_login():
    print("\n--------- USER LOGIN ---------")
    login_email = input("Enter User Email: ")
    login_pass = input("Enter User Password: ")
    # Convert login password into hash
    hashed_password = hash_pass(login_pass)
    # Create database connection
    cursor, con = create_connection()
    cursor.execute(
        """
        SELECT * FROM USERS
        WHERE UEMAIL = ? AND UPASSWORD = ?
        """,
        (login_email, hashed_password)
    )
    user = cursor.fetchone()
    if user:
        print("The Username And Password Is Valid")
        print("Wellocome To Your Account")
    else:
        print("The User Is Not Valid")
        def recursion():
            if counter==3:
                print("Yor login Is Failed You Traid Within next 24 hours")
                break
        recursion()
    con.close()
# -----------------------------------------
# Main
# -----------------------------------------
User_registration()
User_login()