"""
SageManager models for storing data. In addition, this module houses the
functions for creating, updating, deleteing, and reading passwords.
"""


import peewee as pw


DATABASE = pw.SqliteDatabase(None)


class SageManager(pw.Model):
    """
    Main database class for storing passwords. Built on the Peewee ORM.
    """
    NAME = pw.CharField(unique=True)
    PASSWD = pw.CharField()
    class Meta:
        """Peewee Meta Class"""
        database = DATABASE


def init_db(name: str):
    """
    Initialize the module database with a filename.

    Arguments:
        name: Name of the database, string.
    """
    DATABASE.init(name)


def pw_call(models: list):
    """
    Decorator function that handles database related functions like table
    creation, connecting, and closing.

    Arguments:
        models: List of models to use, list.
    Returns:
        Decorated Function.
    """
    def wrapper(func):
        """The actual decorator"""
        def wrapped(*args, **kwargs):
            """Wrapped version of the function."""
            with DATABASE:
                DATABASE.create_tables(models)
                return func(*args, **kwargs)

        return wrapped

    return wrapper


@pw_call([SageManager])
def create_passwd(site_name: str, passwd: str) -> bool:
    """
    Save the password for the given site name. Note that a site name
    does not necessarily need to be a URL, it could be an application
    or even a username.

    Arguments:
        site_name: Name to store the password with
        passwd: Password to store with the name.
    Returns:
        result: A boolean indicating either success or failure
        in creating the password
    """
    if not SageManager.get_or_none(SageManager.NAME == site_name):
        SageManager.create(NAME=site_name, PASSWD=passwd)
        result = True
    else:
        result = False
    return result


@pw_call([SageManager])
def update_passwd(site_name: str, new_passwd: str) -> bool:
    """
    Update the password for the given site name.

    Arguments:
        site_name: Site name to update.
        new_passwd: New password for the site
    Returns:
        result: A boolean indicating either success or failure in
        updating the password.
    """
    query = SageManager.get_or_none(SageManager.NAME == site_name)
    if query:
        query.PASSWD = new_passwd
        query.save()
        result = True
    else:
        result = False
    return result


@pw_call([SageManager])
def read_passwd(site_name: str) -> str:
    """
    Read out the password for a given site, and return a plaintext version
    of it. This function does not add it to the clipboard, it simply
    reads the password.

    Arguments:
        site_name: Site name to read
    Returns:
        result: A string that is the password, or False indicating failure
    """
    query = SageManager.get_or_none(SageManager.NAME == site_name)
    if query:
        result = query.PASSWD
    else:
        result = False
    return result


@pw_call([SageManager])
def remove_passwd(site_name: str) -> bool:
    """
    Remove a password and site from the database.

    Arguments:
        site_name: Site name to delete.
    Returns:
        result: A boolean indicating either success or failure.
    """
    query = SageManager.get_or_none(SageManager.NAME == site_name)
    if query:
        query.delete_instance()
        result = True
    else:
        result = False
    return result
