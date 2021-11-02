import mysql.connector


class DummyMysqlEnv:
    dbname = "test_diary_database"
    def __init__(self):
        # Create test database
        db = mysql.connector.connect(
            host="localhost",
            user="youruser",
            password="yourpassword"
        )

        cursor = db.cursor()
        cursor.execute(f"CREATE DATABASE {self.dbname}")
        cursor.close()
        
        self.db = mysql.connector.connect(
            host="localhost",
            user="youruser",
            password="yourpassword",
            database=self.dbname
        )
        

    def __del__(self):
        cursor = self.db.cursor()
        cursor.execute(f"DROP DATABASE {self.dbname}")
        cursor.close()