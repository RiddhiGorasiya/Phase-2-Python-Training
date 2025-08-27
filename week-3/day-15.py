# # Create Table
# import sqlite3

# # Connect to the SQLite database (or create it if it doesn't exist)
# connection_obj = sqlite3.connect('SQLite.db')
# cursor_obj = connection_obj.cursor()
# # SQL query to create the table
# table_creation_query = """
#     CREATE TABLE EMP (
#         Email VARCHAR(255) NOT NULL,
#         First_Name CHAR(25) NOT NULL,
#         Last_Name CHAR(25),
#         Score INT
#     );
# """
# # Execute the table creation query
# cursor_obj.execute(table_creation_query)
# # Confirm that the table has been created
# print("Table is Ready")
# # Close the connection to the database
# connection_obj.close()

# # Insert Data
# import sqlite3

# # Connect to SQLite database
# conn = sqlite3.connect('SQLite.db')
# cursor = conn.cursor()
# # Insert data into the table
# cursor.execute("INSERT INTO EMP VALUES ('riddhi@gmail.com', 'riddhi', 'gorasiya', '1')")
# cursor.execute("INSERT INTO EMP VALUES ('heni@gmail.com', 'heni', 'nakrani', '2')")
# cursor.execute("INSERT INTO EMP VALUES ('disha@gmail.com', 'disha', 'bhikadiya', '3')")
# cursor.execute("INSERT INTO EMP VALUES ('vaibhav@gmail.com', 'vaibhav', 'gorasiya', '4')")
# # Display inserted data
# print("Data Inserted in the table: ")
# cursor.execute("SELECT * FROM EMP")
# for row in cursor.fetchall():
#     print(row)
# # Commit changes and close connection
# conn.commit()
# conn.close()

# # Deleting Data in Table
# import sqlite3

# # Connecting to sqlite
# connection_obj = sqlite3.connect('SQLite.db')
# # cursor object
# cursor_obj = connection_obj.cursor()
# #delete data
# cursor_obj.execute("DELETE FROM D:\Python Training\Phase-1-Python-Training WHERE Score < 3")
# connection_obj.commit()
# # Close the connection
# connection_obj.close()

# Update Data
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('up.db')
# Creating a cursor object using 
# the cursor() method
cursor = conn.cursor()
# Creating table
table = ("""CREATE TABLE EMPLOYEE(FIRST_NAME VARCHAR(255), 
LAST_NAME VARCHAR(255),AGE int, SEX VARCHAR(255), INCOME int);""")
cursor.execute(table)
# Queries to INSERT records.
cursor.execute(
    '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
    VALUES ('Anand', 'Choubey', 25, 'M', 10000)''')
cursor.execute(
    '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
    VALUES ('Mukesh', 'Sharma', 20, 'M', 9000)''')
cursor.execute(
    '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
    VALUES ('Ankit', 'Pandey', 24, 'M', 6300)''')
cursor.execute(
    '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
    VALUES ('Subhdra ', 'Singh', 26, 'F', 8000)''')
cursor.execute(
    '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
    VALUES ('Tanu', 'Mishra', 24, 'F', 6500)''')
# Display data inserted
print("EMPLOYEE Table: ")
data = cursor.execute('''SELECT * FROM EMPLOYEE''')
for row in data:
    print(row)
# Updating
cursor.execute('''UPDATE EMPLOYEE SET INCOME = 5000 WHERE Age<25;''')
print('\nAfter Updating...\n')
# Display data
print("EMPLOYEE Table: ")
data = cursor.execute('''SELECT * FROM EMPLOYEE''')
for row in data:
    print(row)
# Commit your changes in the database
conn.commit()
# Closing the connection
conn.close()

