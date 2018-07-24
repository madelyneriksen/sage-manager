"""
Main Command Line Entry Point.
"""


import click
from sagemanager import models
from sagemanager import crypto


@click.command()
def main():
    """
    SageManager is a command line password generator and vault, that uses
    gpg encryption on truly random passwords with high entropy.
    """


if __name__ == "__main__":
    main()
