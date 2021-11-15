import pytest
from tests.dummy_mysql_env import DummyMysqlEnv
from utils.update_mysql_table import update_diary, update_tag
from utils.fetch_data import fetch_tag

@pytest.fixture
def content():
    return "a b 怪怪中\n文字\' ，。\n\n\n1 23"

@pytest.fixture
def date():
    return "1993-02-08"

@pytest.fixture
def tags():
    return ["a", "BB", "中文"]

# def test_update_diary():
#     env = DummyMysqlEnv()
#     cursor = env.database().cursor()


def test_update_tag_duplicate(tags):
    env = DummyMysqlEnv()
    db = env.database
    ids = update_tag(db, tags)
    assert ids == [1, 2, 3]
    ids = update_tag(db, reversed(tags))
    assert ids == [3, 2, 1]


def test_update_tag_value(tags):
    env = DummyMysqlEnv()
    db = env.database
    update_tag(db, tags)
    target = fetch_tag(db)
    assert target == tags