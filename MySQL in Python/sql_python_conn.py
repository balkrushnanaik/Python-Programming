import sqlite3

# Create a database in SQL
conn = sqlite3.connect('Test_Database.sqlite')

# Table Name
conn.execute("CREATE TABLE Students(first_name TEXT, last_name TEXT, branch TEXT, marks INTEGER)")

# Commit and Save
conn.commit()
