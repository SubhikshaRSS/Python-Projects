#Connecting database in python
#pip install mysql-connector-python  (in terminal)
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="school"
)

print("Connected to MySQL successfully.")

cursor = connection.cursor()

cursor.execute("SELECT * FROM Students")

for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()