import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
    )
""")
cursor.execute("INSERT INTO users (name, age) VALUES ('riddhi', 20)")
cursor.execute("INSERT INTO users (name, age) VALUES ('heni', 21)")
conn.commit()
cursor.execute("SELECT * FROM users")   
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()