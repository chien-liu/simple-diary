import mysql.connector
from utils.create_database import create_diarydatabase

class DummyMysqlEnv:
    dbname = "test_diary_database"
    def __init__(self):
        # Create test database
        self.database = create_diarydatabase(self.dbname)
        

    def __del__(self):
        cursor = self.database.cursor()
        cursor.execute(f"DROP DATABASE {self.dbname}")
        cursor.close()