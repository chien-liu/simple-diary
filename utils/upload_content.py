from typing import Tuple, List
import mysql.connector

# Type alias
Database = mysql.connector.connection.MySQLConnection

def upload_content(filename: str, db: Database):
    date, tags, content = _decode(filename)
    # Update tables
    diary_id = _update_diary(db, date, content)
    tags_id = _update_tag(db, tags)
    _update_diary_tags(db, diary_id, tags_id)

def _decode(filename: str) -> Tuple[str, List[str], str]:
    with open(filename) as f:
        lines = f.readlines()
        
        date = lines[2].strip()
        assert date[:5] == "Date:"
        if len(date) > len("Date:"):
            date = date[5:].replace(" ", "")
        else:
            date = ""

        tags = lines[3].strip()
        assert tags[:5] == "Tags:"
        if len(tags) > len("Tags:"):
            tags = tags[5:].strip().split(" ")
        else:
            tags = []

        content = lines[4]
        assert content[:8] == "Content:"
        content = "".join(lines[5:])
    return date, tags, content

def _update_diary(db: Database, date: str, content: str) -> int:
    cursor = db.cursor()
    
    sql = "INSERT INTO diary (date, content) VALUES (%s, %s)"
    val = (date, content)
    cursor.excute(sql, val)
    cursor.commit()

    sql = "SELECT LAST_INSERT_ID() from diary"
    cursor.excute(sql)
    id = cursor.fetchall()  # TODO type convert
    
    return id

def _update_tags(db: Database, tags: List[str]) -> List[int]:
    pass