import sqlite3

con=sqlite3.Connection("demo.db")
print("Step1:-Database Is Created")

cursor=con.cursor()
print("Step2:-Cursor Is creted")

# cursor.execute(
#     '''CREATE TABLE swapnil1(id INTEGER,name TEXT)
#     ''')
# print("Step3:-table is created Sucessfullly")

# cursor.execute('''INSERT INTO swapnil(id,name) values(101,"swapnil")''')
# print("data Inserted Sucessfully")

# cursor.execute('''SELECT * FROM swapnil1''')
# data=cursor.fetchall()
# print(data)

cursor.execute('''INSERT INTO swapnil(id,name) values(?,?),(102,"swapnil")''')
print("Valuse Inserted Sucesffuly")
con.close()