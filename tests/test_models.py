"""
Pytest module to test the models and database.

We use a pytest fixture for managing state, because otherwise
the databases would continue to exist, and the in memory database wouldn't work
if the functions had a database.close() call.

Thankfully, fixtures are an awesome feature of pytest!
"""


import os
import pytest
import sagemanager.models as smm


@pytest.fixture(scope="module")
def sqlite_db():
    """
    Database manager that oversees teardowns and cleanup.

    This allows us to persist the same database over the course of the tests,
    which while not strictly a unit test is still useful for overseeing the
    CRUD calls that need to be made.

    Yields:
        database: An sqlite database for testing
    """
    smm.init_db("test.db")
    yield smm.DATABASE
    os.remove("test.db")


def test_creation(sqlite_db):
    """
    Test the creation of passwords. The password is module level, so tests
    in the future can use the same password.
    """
    new_pass = "TheNewPassword"
    site = "www.example.com"
    response = smm.create_passwd(site, new_pass)
    assert response
    # Make sure we can't create twice.
    bad_response = smm.create_passwd(site, new_pass)
    assert not bad_response


def test_read(sqlite_db):
    """
    Test the reading of passwords.
    """
    site = "www.example.com"
    passwd = smm.read_passwd(site)
    assert passwd == "TheNewPassword"
    bad_request = smm.read_passwd("NotASite")
    assert not bad_request


def test_update(sqlite_db):
    """
    Test the updating of passwords
    """
    updated_pass = "TheUpdatedPassword"
    site = "www.example.com"
    response = smm.update_passwd(site, updated_pass)
    assert response
    assert smm.read_passwd(site) == updated_pass
    bad_response = smm.update_passwd("NotASite", updated_pass)
    assert not bad_response


def test_removal(sqlite_db):
    """
    Test the removal of passwords.
    """
    site = "www.example.com"
    response = smm.remove_passwd(site)
    assert response
    bad_response = smm.remove_passwd(site)
    assert not bad_response
    assert not smm.read_passwd(site)
