import pymssql
import os
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

def fetch_employees():
    try:
        # Retrieve credentials from environment variables
        server = os.environ.get('DB_SERVER')
        database = os.environ.get('DB_NAME')
        username = os.environ.get('DB_USER')
        password = os.environ.get('DB_PASSWORD')

        if not all([server, database, username, password]):
            print("Database credentials are not fully set in environment variables.")
            return []

        connection = pymssql.connect(
            server=server,
            user=username,
            password=password,
            database=database
        )
        
        cursor = connection.cursor(as_dict=True)
        cursor.execute("SELECT TOP 5 * FROM Employees")
        results = cursor.fetchall()
        
        connection.close()
        return results
    except Exception as e:
        print("Database connection error:", e)
        return []
