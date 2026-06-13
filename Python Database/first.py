import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin",
    database="logic_building"
)

print("Connected Successfully!")

conn.close()