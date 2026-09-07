import sqlite3

con = sqlite3.connect("ABC.db")

print("Database Connected")

cursor = con.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ABC(
        id INTEGER PRIMARY KEY,
        name TEXT,
        salary INTEGER
    )
""")

print("Table Created")

# Insert data
cursor.execute("""
    INSERT INTO ABC(id, name, salary)
    VALUES(1, 'SWAP', 102)
""")

con.commit()
print("Data Inserted")
# Check data
cursor.execute("SELECT * FROM ABC")
#To Fetch The Data From Database
data = cursor.fetchall()
print("Data:", data)
con.close()