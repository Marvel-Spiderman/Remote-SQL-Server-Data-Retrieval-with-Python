import pymssql
import os
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

fallback_data = [
    {"id": 1, "name": "Alice Smith", "email": "alice@example.com", "department": "Engineering", "position": "Software Engineer", "hire_date": "2022-01-15", "salary": 95000},
    {"id": 2, "name": "Bob Johnson", "email": "bob@example.com", "department": "Marketing", "position": "Marketing Manager", "hire_date": "2021-03-22", "salary": 85000},
    {"id": 3, "name": "Charlie Brown", "email": "charlie@example.com", "department": "Sales", "position": "Sales Rep", "hire_date": "2023-06-10", "salary": 60000},
    {"id": 4, "name": "Diana Prince", "email": "diana@example.com", "department": "HR", "position": "HR Specialist", "hire_date": "2020-11-05", "salary": 75000},
    {"id": 5, "name": "Evan Wright", "email": "evan@example.com", "department": "Engineering", "position": "DevOps Engineer", "hire_date": "2019-08-19", "salary": 105000}
]

def fetch_employees():
    try:
        # Retrieve credentials from environment variables
        server = os.environ.get('DB_SERVER')
        database = os.environ.get('DB_NAME')
        username = os.environ.get('DB_USER')
        password = os.environ.get('DB_PASSWORD')

        if not all([server, database, username, password]):
            print("Database credentials are not fully set. Returning predefined data.")
            return fallback_data

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
        print("Database connection error:", e, "Returning predefined data.")
        return fallback_data

