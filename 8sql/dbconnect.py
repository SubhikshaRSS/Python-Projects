import mysql.connector  #pip install mysql-connector-python
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="school"
    )

    print("Connected to MySQL successfully.")
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Fees")

        for row in cursor.fetchall():
            print(row)

        cursor.close()
        connection.close()
    else:
        print("Failed to connect to MySQL.")
        exit()
except:
    print(f"Error connecting to MySQL:")
    exit()
