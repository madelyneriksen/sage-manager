"""
Main Cryptographic functions for the SageManager library.

SystemRandom() is used for generating cryptographically secure password choices.
The level of security may not be the same on all systems.

Encryption itself is done with GPG encryption, using a user entered password
for encrypting/decrypting passwords.
"""


import random
import string
import base64
import gnupg


def encrypt_passwd(passwd: string, key: string) -> str:
    """
    Encrypt the generated password with the provided key. (A key is essentially
    another password.)

    Arguments:
        passwd: Password to encrypt, A string
        key: Key for encrypting, A string
    Returns:
        encrypted: A base64 string that's the encoded password.
    """
    pass

def decrypt_passwd(passwd: string, key: string) -> str:
    """
    Decrypt the passwd with the provided key.

    Arguments:
        passwd: Password to decrypt, A string
        key: Key for decrypting, A string
    Returns:
        decrypted: Decrypted password, in utf-8
    """
    pass
