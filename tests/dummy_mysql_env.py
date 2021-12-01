import mysql.connector
from itertools import count
from utils.create_database import create_diarydatabase

class DummyMysqlEnv:
    dbname = "test_diary_database"
    def __init__(self):
        for i in count():
            print(i)
            DBNAME = self.dbname + str(i)
            # Create test database
            self.database = create_diarydatabase(DBNAME)
            if self.database is not None:
                break
        

    def __del__(self):
        cursor = self.database.cursor()
        cursor.execute(f"DROP DATABASE {self.dbname}")
        cursor.close()