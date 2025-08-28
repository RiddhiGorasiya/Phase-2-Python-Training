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

# Connect to SQLite database
conn = sqlite3.connect('SQLite.db')
cursor = conn.cursor()
# Insert data into the table
cursor.execute("INSERT INTO EMP VALUES ('riddhi@gmail.com', 'riddhi', 'gorasiya', '1')")
cursor.execute("INSERT INTO EMP VALUES ('heni@gmail.com', 'heni', 'nakrani', '2')")
cursor.execute("INSERT INTO EMP VALUES ('disha@gmail.com', 'disha', 'bhikadiya', '3')")
cursor.execute("INSERT INTO EMP VALUES ('vaibhav@gmail.com', 'vaibhav', 'gorasiya', '4')")
# Display inserted data
print("Data Inserted in the table: ")
cursor.execute("SELECT * FROM EMP")
for row in cursor.fetchall():
    print(row)
# Commit changes and close connection
conn.commit()
conn.close()

