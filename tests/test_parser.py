import pytest
import mysql.connector
from utils.parser import ContentParser
# Type alias
Database = mysql.connector.connection.MySQLConnection

# @pytest.
# def dummy_diary() -> Database:
#     pass

def test_decode_null():
    filename = "tests/blank-diary.txt"
    date, tags, content = ContentParser()(filename)
    assert date == ""
    assert tags == []
    assert content == ""

def test_decode_lorem():
    filename = "tests/lorem-diary.txt"
    date, tags, content = ContentParser()(filename)
    assert date == "1234-56-78"
    assert tags == ["A", "B", "C"]
    assert content == "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nCurabitur gravida est nec nunc vulputate suscipit."