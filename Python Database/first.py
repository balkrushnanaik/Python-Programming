# import mysql.connector
#
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Admin",
#     database="logic_building"
# )
#
# print("Connected Successfully!")
#
# conn.close()
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="company"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM employees")

for row in cursor.fetchall():
    print(row)

conn.close()