import random
import string
import gnupg
pgp = gnupg.GPG()
from os import system

info = open('Alice', 'r')
passphrase = info.readlines()[2].replace("passphrase: ", '')
print(passphrase)

# decrypt
with open('encrypted.gpg.txt', 'rb') as f:
    status = pgp.decrypt_file(
        file=f,
        passphrase=''.join(passphrase),
        output='decrypted.txt'
    )
