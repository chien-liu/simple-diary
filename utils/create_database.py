import mysql.connector

def create_diarydatabase(name: str = "diarydatabase"):
    # Create test database
        db = mysql.connector.connect(
            host="localhost",
            user="youruser",
            password="yourpassword"
        )

        cursor = db.cursor()
        cursor.execute(f"CREATE DATABASE {name}")
        cursor.close()
        
        db = mysql.connector.connect(
            host="localhost",
            user="youruser",
            password="yourpassword",
            database=name
        )
        return db