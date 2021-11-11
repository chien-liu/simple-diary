from typing import Tuple, List
import mysql.connector


# Type alias
Database = mysql.connector.connection.MySQLConnection

def update_diary(db: Database, date: str, content: str) -> int:
    cursor = db.cursor()
    
    sql = "INSERT INTO diary (date, content) VALUES (%s, %s)"
    val = (date, content)
    cursor.execute(sql, val)
    cursor.commit()

    sql = "SELECT LAST_INSERT_ID() from diary"
    cursor.execute(sql)
    id = cursor.fetchall()  # TODO type convert
    assert len(id) == 1
    return id[0]

def update_tag(db: Database, tags: List[str]) -> List[int]:
    cursor = db.cursor()
    ids = []
    for t in tags:
        sql = "INSERT IGNORE INTO tag (name) VALUES (%s)"
        cursor.execute(sql, (t,))
        db.commit()

        id = cursor.lastrowid
        cursor.execute("SELECT * from tag")
        print(cursor.fetchall())
        if not id:
            sql = f"SELECT id FROM tag WHERE name=\'{t}\'"
            print(sql)
            cursor.execute(sql)
            result = cursor.fetchall()  # result = [(tag,)]
            assert len(result) == 1
            id = result[0][0]
        print(id)
        ids.append(id)
    return ids
