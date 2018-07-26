"""
Test the integration part of the module.

These tests are slightly more time consuming because they are not unit tests
in a strict (or any) sense of the word. However, the UX depends heavily on
interaction of components, so this is essential.
"""
import os
import string
import pytest
import pyperclip
import sagemanager.models as models
import sagemanager.integrations as integrate


KEY = "PlaintextPassword"
SITE = "www.example.com"


@pytest.fixture(scope="module")
def sqlite_db():
    """
    Database manager that oversees teardowns and cleanup.

    Yields:
        database: An sqlite database for testing
    """
    models.init_db("test.db")
    yield models.DATABASE
    os.remove("test.db")


def validate_passwd(passwd: str) -> bool:
    """
    Quick helper function for password validation.
    """
    alpha = string.ascii_letters + string.digits + string.punctuation
    checker = passwd.split('')
    return all([i in alpha for i in checker])


def test_authorization(sqlite_db):
    """
    Create a token and use it to authorize.
    """
    assert integrate.store_token(KEY)
    assert integrate.verify_passwd(KEY)
    assert not integrate.verify_passwd("NotAPassword")


def test_create_passwd(sqlite_db):
    """
    Create a password and save it.
    """
    assert integrate.create_encrypted_passwd(SITE, KEY)
    assert not integrate.create_encrypted_passwd(SITE, "WrongKey")


def test_get_passwd(sqlite_db):
    """
    Read the password created above.
    """
    result = integrate.get_encrypted_passwd(SITE, KEY)
    assert result
    if result:
        clipboard = pyperclip.paste()
        assert validate_password(clipboard)
    assert not integrate.get_encrypted_passwd(SITE, "WrongKey")
    assert not integrate.get_encrypted_passwd("WrongSite", KEY)


def test_update_passwd(sqlite_db):
    """
    Update an existing password.
    """
    integrate.get_encrypted_passwd(SITE, KEY)
    old_passwd = pyperclip.paste()
    assert integrate.update_encrypted_passwd(SITE, KEY)
    integrate.get_encrypted_passwd(SITE, KEY)
    new_passwd = pyperclip.paste()
    assert new_passwd != old_passwd
    assert not integrate.update_encrypted_passwd(SITE, "WrongKey")
    assert not integrate.update_encrypted_passwd("WrongSite", "WrongKey")



