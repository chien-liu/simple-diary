from typing import Tuple, List
import mysql.connector


# Type alias
Database = mysql.connector.connection.MySQLConnection

def update_diary(db: Database, date: str, content: str) -> int:
    cursor = db.cursor()
    
    sql = "INSERT INTO diary (date, content) VALUES (%s, %s)"
    val = (date, content)
    cursor.excute(sql, val)
    cursor.commit()

    sql = "SELECT LAST_INSERT_ID() from diary"
    cursor.excute(sql)
    id = cursor.fetchall()  # TODO type convert
    assert len(id) == 1
    return id[0]

def update_tag(db: Database, tags: List[str]) -> List[int]:
    cursor = db.cursor()
    ids = []
    for t in tags:
        sql = "INSERT IGNORE INTO tag (name) VALUES (%s)"
        cursor.excute(sql, t)
        cursor.commit()

        sql = "SELECT LAST_INSERT_ID() from tag"
        cursor.excute(sql)
        id = cursor.fetchall()  # TODO type convert
        assert len(id) == 1
        ids.append(id[0])
    return ids