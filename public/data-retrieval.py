import mysql.connector
from mysql.connector import Error

def fetch_feedback():
    """Connects to MySQL and retrieves player_feedback data."""
    connection = None
    try:
        # Hostinger MySQL connection details
        connection = mysql.connector.connect(
            host='localhost', # Usually 'localhost' on Hostinger [5]
            database='u123456789_dbname',
            user='u123456789_dbuser',
            password='your_secure_password'
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM player_feedback"
            cursor.execute(query)
            
            # Retrieve all rows [1, 3]
            records = cursor.fetchall()
            
            print(f"Total rows: {cursor.rowcount}")
            for row in records:
                print(row)

    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    finally:
        # Close connection [4, 6, 9]
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    fetch_feedback()
