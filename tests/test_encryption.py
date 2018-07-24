"""
Test the encryption functions of SageManager
"""


import pytest
from sagemanager.crypto import encrypt_passwd, decrypt_passwd


def test_encryption():
    """
    Test the encryption and decryption functions.
    """
    key = "ThisWouldBeAUserPassword"
    bad_key = "ThisIsNotThePassword"
    passwd = "RandomStringPassword"
    encrypted = encrypt_passwd(passwd, key)
    decrypted = decrypt_passwd(encrypted, key)
    bad_decrypted = decrypt_passwd(encrypted, bad_key)
    assert isinstance(encrypted, str)
    assert isinstance(decrypted, str)
    assert encrypted != passwd
    assert decrypted == passwd
    assert bad_decrypted != passwd
