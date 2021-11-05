import mysql.connector


# Type alias
Cursor = mysql.connector.cursor_cext.CMySQLCursor

def create_diarydatabase(DB_NAME: str = "diarydatabase"):
    # Create test database
    db = mysql.connector.connect(
        host="localhost",
        user="youruser",
        password="yourpassword"
    )

    cursor = db.cursor()
    try:
        cursor.execute(f"CREATE DATABASE {DB_NAME}")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

    try:
        cursor.execute(f"USE {DB_NAME}")
    except mysql.connector.Error as err:
        print(err)

    return db    