"""
Putting it all together, this module combines the centryption and reading
functions from other parts of the library to create functionality.
"""

from getpass import getpass
import pyperclip
import sagemanager.models as models
import sagemanager.crypto as crypto


def get_encrypted_passwd(site_name: str, key: str) -> bool:
    """
    Grab the password and decrypt it, then copy it to the clipboard.

    Arguments:
        site_name: Name of the site to get the password from
        key: The user's key for decryption

    Returns:
        result: True or False indicating success or failure.
    """
    pass


def create_encrypted_passwd(site_name: str, key: str) -> bool:
    """
    Create an encrypted password and save it with the user's key.

    Arguments:
        site_name: Name of the site to save a password for.
        key: The user's key for encryption.

    Returns:
        result: True or False indicating success or failure.
    """
    pass


def update_encrypted_passwd(site_name: str, key: str) -> bool:
    """
    Update a password, encrypt it, and save it with the user's key.

    Arguments:
        site_name: Name of the site to update.
        key: The user's key for encryption.

    Returns:
        result: True or False indicating success or failure.
    """
    pass


def verify_passwd(key: str) -> bool:
    """
    Read a dummy argument and see if it matches the user's key.

    Arguments:
        key: The user's key for encryption.

    Returns:
        result: True or False indicating success or failure.
    """
    pass


def store_token(key: str) -> bool:
    """
    Store a dummy token that's used for verifying keys match.

    Arguments:
        key: The user's key for encryption.

    Returns:
        result: True or False indicating success or failure.
    """


def get_key() -> str:
    """
    Get the user's key from the input prompt.

    Returns:
        key: The user's key for encryption.
    """
    pass
