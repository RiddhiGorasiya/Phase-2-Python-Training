import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("sqlite.db")
cursor = conn.cursor()
# Create table
cursor.execute("""CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255), SECTION VARCHAR(255))""")
# Insert data into the table
cursor.execute("INSERT INTO STUDENT VALUES ('riddhi', '7th', 'A')")
cursor.execute("INSERT INTO STUDENT VALUES ('disha', '8th', 'B')")
cursor.execute("INSERT INTO STUDENT VALUES ('heni', '9th', 'C')")
print("Data Inserted in the table: ")
cursor.execute("SELECT * FROM STUDENT")
for row in cursor.fetchall():
    print(row)
conn.commit()
conn.close()