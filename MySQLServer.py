import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host='localhost', # Update this if your MySQL server is running on a different host
            user='your_username', # Update with your MySQL username
            password='your_password' # Update with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
