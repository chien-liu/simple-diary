from typing import Tuple, List
import mysql.connector

from utils.parser import ContentParser
from utils.update_mysql_table import update_diary, update_tag

# Type alias
Database = mysql.connector.connection.MySQLConnection

def upload_content(filename: str, db: Database):
    date, tags, content = ContentParser()(filename)
    # Update tables
    diary_id = update_diary(db, date, content)
    tags_id = update_tag(db, tags)
    _update_diary_tags(db, diary_id, tags_id)

