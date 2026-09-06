import sqlite3
# Connecting To DataBase
con = sqlite3.connect("ABC.db")
print("Connection Is Created Successfully")
# Cursor Object Is Creating
cursor = con.cursor()
id = input("Enter The Id: ")
name = input("Enter The Name: ")
salary = input("Enter The Salary: ")
cursor.execute(
    """
    INSERT INTO ABC(id, name, salary)
    VALUES (?, ?, ?)
    """,
    (id, name, salary)
)
print("Data Added Successfully")
#Save the Data
con.commit()
#Coonetion Is Close Here
con.close()