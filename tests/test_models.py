"""
Pytest module to test the models and database.

We use a pytest fixture for managing state, because otherwise
the databases would continue to exist, and the in memory database wouldn't work
if the functions had a database.close() call.

Thankfully, fixtures are an awesome feature of pytest!
"""


import peewee as pw
from sagemanager.models import SageManager


@pytest.fixture(scope=module)
def sqlite_db():
    """
    Database manager that oversees teardowns and cleanup.

    This allows us to persist the same database over the course of the tests,
    which while not strictly a unit test is still useful for overseeing the
    CRUD calls that need to be made.

    Yields:
        database: An sqlite database for testing
    """
    database = pw.SqliteDatabase("test.db")
    yield database
    os.remove("test.db")


def test_creation(sqlite_db):
    pass


def test_read(sqlite_db):
    pass


def test_removal(sqlite_db):
    pass


def test_update(sqlite_db):
    pass
