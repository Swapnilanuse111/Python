import sqlite3
con=sqlite3.connect("Connectivlty.db")
print("DataBase Is Created/Connection is estsblidhs")

#Creating Cursor Object From The con 
coursor=con.cursor()

print("Coursor Is Created")

#Lets Creating The Table 
con.execute('''
            CREATE TABLE  employee(id INTEGER PRIMARY KEY,
            name TEXT,
            sal INTERGER)
        ''')
print("Table Is Created Sucesfully")

#Lets Add Some Data Inside the Table

con.execute('''
        INSERT INTO employee(id,name,sal) VALUES(101,"Rahul",2000000)
''')
print("Data Insrted Sucessfully")

con.commit()
con.close()