import mysql.connector
from mysql.connector import errorcode

# Type alias
Cursor = mysql.connector.cursor.MySQLCursor

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

    create_table(cursor)

    return db


def create_table(cursor: Cursor):
    # https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html
    TABLES = dict()
    TABLES["diary"] = (
        "CREATE TABLE diary ("
        "    id INT UNSIGNED AUTO_INCREMENT,"
        "    date DATE NOT NULL,"
        "    content LONGTEXT NOT NULL,"
        "    PRIMARY KEY(id),"
        "    UNIQUE (date)"
        ")"
    )

    TABLES["tag"] = (
        "CREATE TABLE tag ("
        "    id INT UNSIGNED AUTO_INCREMENT,"
        "    name VARCHAR(40) NOT NULL,"
        "    PRIMARY KEY(id),"
        "    UNIQUE (name)"
        ")"
    )

    TABLES["diary_tag"] = (
        "CREATE TABLE diary_tag ("
        "    diary_id INT UNSIGNED NOT NULL,"
        "    tag_id INT UNSIGNED NOT NULL,"
        "    UNIQUE (diary_id, tag_id)"
        ")"
    )

    for table_name, table_description in TABLES.items():
        try:
            print(f"Creating table {table_name}")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
