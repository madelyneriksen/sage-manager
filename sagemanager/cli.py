"""
Main Command Line Entry Point for SageManager.

There's a lot of logic bundled into the function "main" still. This can likely
get pushed back into integrations, but it makes sense from a logical perspective
for the function to be arranged as it is, because it's really only an "if this,
do that".
"""


import sys
from os.path import expanduser
import click
import sagemanager.models as models
import sagemanager.integrations as integrate


# Initialize database for the user's home directory
models.init_db(expanduser("~")+"/.sagemanager.db")


@click.command()
@click.option("--create", help="Create a password for a given site name.")
@click.option("--update", help="Generate a new password for a given site name.")
@click.option("--get", help="Copy a password to the clipboard.")
def main(create, update, get):
    """
    SageManager is a command line password generator and vault, that uses
    gpg encryption on truly random passwords with high entropy.
    """
    # Token Creation
    if any([create, update, get]):
        key = integrate.get_key()
        token_exists = integrate.check_token()
        if not token_exists:
            integrate.store_token(key)
    # Create a password if create is on.
    if create:
        result = integrate.create_encrypted_passwd(create, key)
        if not result:
            click.echo("Password creation for {} failed! Check your password,"
                       "and make sure not to create a password twice!".format())
            sys.exit(1)
        else:
            click.echo("Password creation for {} success!".format(create))
            sys.exit(0)
    # Update a password if update is on.
    if update:
        result = integrate.update_encrypted_passwd(update, key)
        if not result:
            click.echo("Update for {} failed! Check your password, and"
                       "make sure the site name exists.".format(update))
            sys.exit(1)
        else:
            click.echo("Password update for {} success!".format(update))
            sys.exit(0)
    # Copy a password to the clipboard if get is on
    if get:
        result = integrate.get_encrypted_passwd(get, key)
        if not result:
            click.echo("Password retrieval for {} failed! Check your password,"
                       "and make sure the site name exists.".format(get))
            sys.exit(1)
        else:
            click.echo("Password for {} copied to clipboard!".format(get))
            sys.exit(0)


if __name__ == "__main__":
    main()
