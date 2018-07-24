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


# Constants
GPG = gnupg.GPG()



def encrypt_passwd(passwd: str, key: str) -> str:
    """
    Encrypt the generated password with the provided key. (A key is essentially
    another password.)

    Arguments:
        passwd: Password to encrypt, A string
        key: Key for encrypting, A string
    Returns:
        encrypted: A base64 string that's the encoded password.
    """
    encrypted = GPG.encrypt(passwd, symmetric=True,
                            passphrase=key, encrypt=False)
    return base64.b64encode(encrypted.data).decode()


def decrypt_passwd(passwd: str, key: str) -> str:
    """
    Decrypt the passwd with the provided key.

    Arguments:
        passwd: Password to decrypt, A string
        key: Key for decrypting, A string
    Returns:
        decrypted: Decrypted password, in utf-8
    """
    decrypted = GPG.decrypt(base64.b64decode(passwd), passphrase=key)
    return decrypted.data.decode()


def create_passwd(length=24) -> str:
    """
    Create a password that is (length) long using the cryptographically
    secure system RNG.

    Arguments:
        length: Number of desired characters, Interger. Default 24.
    Returns:
        passwd: (Length) character string of letters, digits, and punctuation
    """
    alpha = string.ascii_letters + string.digits + string.punctuation
    passwd = "".join(
        [random.SystemRandom().choice(alpha) for i in range(length)]
    )
    return passwd
