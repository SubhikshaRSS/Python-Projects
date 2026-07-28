print("Hello mam")
import mysql.connector  #pip install mysql-connector-python
print("db connector")
try:
    
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        database="school",
        port=3306,
        use_pure=True
    )

    print("Connected to MySQL successfully.")

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT VERSION()")
        print("MySQL version:", cursor.fetchone())
        cursor.execute("SELECT * FROM Students")

        for row in cursor.fetchall():
            print(row)

        cursor.close()
        connection.close()
    else:
        print("Failed to connect to MySQL.")
        exit()
except Error as e: # type: ignore
    print(f"Error connecting to MySQL: {e}")
    exit()

finally:
    if 'conn' in locals() and connection.is_connected():
        connection.close()  