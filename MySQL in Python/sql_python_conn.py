import sqlite3
import pandas as pd

# Create a database in SQL
# conn = sqlite3.connect('Test_Database.sqlite')

# Table Name
# conn.execute("CREATE TABLE Students(first_name TEXT, last_name TEXT, branch TEXT, marks INTEGER)")

# Commit and Save
# conn.commit()

# Insert values into the table

# data = conn.cursor()
#
# data.execute(
#     """
#     INSERT INTO Students VALUES
#     ("Balkrushna", "Naik", "CS", 89),
#     ("Soumya", "Singh", "IT", 98),
#     ("Akash", "Tupe", "CS", 80),
#     ("Harshali", "Rahate", "CE", 97)
#     """
# )
# conn.commit()

# Select data
conn = sqlite3.connect('Test_Database.sqlite')

query = """
     SELECT * FROM Students
"""

data1 = pd.read_sql(query,conn)
print(data1)




