import sqlite3

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect("student.db")

# Create cursor
cursor = conn.cursor()

# Example query
cursor.execute("SELECT * FROM students")

# Fetch all records
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close connection
conn.close()