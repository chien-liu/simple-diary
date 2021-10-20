import pytest
import mysql.connector
from utils.upload_content import _decode

# Type alias
Database = mysql.connector.connection.MySQLConnection

# @pytest.
# def dummy_diary() -> Database:
#     pass

def test_decode_null():
    filename = "tests/blank-diary.txt"
    date, tags, content = _decode(filename)
    assert date == ""
    assert tags == []
    assert content == ""
