import mysql.connector
from mysql.connector import Error

def connect_mysql(host, user, password, database):
    try:
        # Establish connection
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if conn.is_connected():
            print(f"Connected to MySQL database: {database}")
            return conn

    except Error as e:
        print(f"MySQL error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Replace with your MySQL credentials
    connection = connect_mysql(
        host="127.0.0.1",
        user="root",
        password="123456",
        database="school"
    )
    if connection:
        connection.close()