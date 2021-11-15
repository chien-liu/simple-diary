from typing import Tuple, List
import mysql.connector


# Type alias
Database = mysql.connector.connection.MySQLConnection


def fetch_tag(db: Database):
    cursor = db.cursor()
    sql = "SELECT name FROM tag"
    cursor.execute(sql)
    fetch = cursor.fetchall()
    tags = [ele[0] for ele in fetch]
    return tags