"""
SageManager models for storing data. In addition, this module houses the
functions for creating, updating, deleteing, and reading passwords.
"""


import peewee as pw


class SageManager(pw.Model):
    """
    Main database class for storing passwords. Built on the Peewee ORM.
    """
    NAME = pw.CharField(unique=True)
    PASSWD = pw.CharField()


def create_passwd(site_name: str, passwd: str, key: str) -> bool:
    """
    Save the password for the given site name. Note that a site name
    does not necessarily need to be a URL, it could be an application
    or even a username.

    Arguments:
        site_name: Name to store the password with
        passwd: Password to store with the name.
        key: Key for accessing, reading, and encrypting the data.
    Returns:
        result: A boolean indicating either success or failute
        in creating the password
    """
    pass


def update_passwd(site_name: str, new_passwd: str, key: str) -> bool:
    """
    Update the password for the given site name.

    Arguments:
        site_name: Site name to update.
        new_passwd: New password for the site
        key: Key for accessing, reading, and encrypting data
    Returns:
        result: A boolean indicating either success or failure in
        creating the password.
    """
    pass

def read_passwd(site_name: str, key: str) -> str:
    """
    Read out the password for a given site, and return a plaintext version
    of it. This function does not add it to the clipboard, it simply
    decrypts and reads the password.

    Arguments:
        site_name: Site name to read
        key: Key for accessing, reading, and encrypting data
    Returns:
        password: A string that is the decrypted, plaintext password.
    """
    pass


def remove_password(site_name: str, key: str) -> bool:
    """
    Remove a password and site from the database.

    Arguments:
        site_name: Site name to delete.
        key: Key for deleting data.
    Returns:
        result: A boolean indicatin either success or failure.
    """
    pass
