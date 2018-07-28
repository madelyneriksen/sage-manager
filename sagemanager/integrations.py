"""
Putting it all together, this module combines the centryption and reading
functions from other parts of the library to create functionality.
"""

from getpass import getpass
import pyperclip
import sagemanager.models as models
import sagemanager.crypto as crypto

# This is an ID for the token that allows password checking.
TOKEN_ID = "INTERNAL_TOKEN"


def check_token() -> bool:
    """
    Check if a token has been created before.

    Returns:
        result: False if no token has been created before.
    """
    result = models.read_passwd(TOKEN_ID)
    return result


def store_token(key: str) -> bool:
    """
    Store a dummy token that's used for verifying keys match.

    Arguments:
        key: The user's key for encryption.

    Returns:
        result: True or False indicating success or failure.
    """
    token = crypto.create_passwd()
    token = crypto.encrypt_passwd(token, key)
    result = models.create_passwd(TOKEN_ID, token)
    return result


def verify_passwd(key: str) -> bool:
    """
    Read the token and see if it matches the user's key.

    Arguments:
        key: The user's key for encryption.

    Returns:
        result: True or False indicating success or failure.
    """
    if not check_token():
        store_token(key)
    token = models.read_passwd(TOKEN_ID)
    decrypted = crypto.decrypt_passwd(token, key)
    return bool(decrypted)


def get_key() -> str:
    """
    Get the user's key from the input prompt.

    Returns:
        key: The user's key for encryption.
    """
    while True:
        passwd_first = getpass()
        passwd_second = getpass("Retype Password:")
        if passwd_first == passwd_second:
            return passwd_first
        else:
            print("Passwords don't match!")


def get_encrypted_passwd(site_name: str, key: str) -> bool:
    """
    Grab the password and decrypt it, then copy it to the clipboard.

    Arguments:
        site_name: Name of the site to get the password from
        key: The user's key for decryption

    Returns:
        result: True or False indicating success or failure.
    """
    verified = verify_passwd(key)
    if verified:
        passwd = models.read_passwd(site_name)
        if passwd:
            passwd = crypto.decrypt_passwd(passwd, key)
            pyperclip.copy(passwd)
            result = True
        else:
            result = False
    else:
        result = False
    return result


def create_encrypted_passwd(site_name: str, key: str) -> bool:
    """
    Create an encrypted password and save it with the user's key.

    Arguments:
        site_name: Name of the site to save a password for.
        key: The user's key for encryption.

    Returns:
        result: True or False indicating success or failure.
    """
    verified = verify_passwd(key)
    if verified:
        passwd = crypto.create_passwd()
        passwd = crypto.encrypt_passwd(passwd, key)
        result = models.create_passwd(site_name, passwd)
    else:
        result = False
    return result


def update_encrypted_passwd(site_name: str, key: str) -> bool:
    """
    Update a password, encrypt it, and save it with the user's key.

    Arguments:
        site_name: Name of the site to update.
        key: The user's key for encryption.

    Returns:
        result: True or False indicating success or failure.
    """
    verified = verify_passwd(key)
    if verified:
        passwd = crypto.create_passwd()
        passwd = crypto.encrypt_passwd(passwd, key)
        result = models.update_passwd(site_name, passwd)
    else:
        result = False
    return result
