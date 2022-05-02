import sys
import random
import string
import gnupg
pgp = gnupg.GPG()
from os import system


print(sys.argv)
emails = [
    "@protonmail.com",
    "@gmail.com",
    "@bu.edu",
    "@yahoo.com",
    "@ed.ac.uk",
    "@godaddy.com",
    "@outlook.com"
]

def gen_email_ending(emails):
    return random.choice(emails)


def gen_id(emails):
    length = random.choice(range(6,13))
    id = ''.join(random.choice(string.ascii_uppercase +
                string.ascii_lowercase + string.digits) for _ in range(length))
    return id + gen_email_ending(emails)


def gen_passhphrase():
    letter_count = random.choice(range(32,64))
    passphrase = ''.join(random.choice(string.ascii_uppercase +
                string.ascii_lowercase) for _ in range(letter_count))

    return passphrase

#id = gen_id(emails)
id = sys.argv[2]
passphrase = gen_passhphrase()
keyserver = 'keyserver.ubuntu.com'
print(id)
print(passphrase)
print(keyserver)
# generate key
input_data = pgp.gen_key_input(
    name_email=''.join(id),
    passphrase=''.join(passphrase),
)
key = pgp.gen_key(
    input_data,
)
print(key)
print(len(pgp.list_keys()))
# ascii readable public and private keys
ascii_armored_public_keys = pgp.export_keys(key.fingerprint)
ascii_armored_private_keys = pgp.export_keys(
    keyids=key.fingerprint,
    secret=True,
    passphrase=passphrase,
)

# export
with open('mykeyfile.asc', 'w') as f:
    f.write(ascii_armored_public_keys)
    f.write(ascii_armored_private_keys)

print(ascii_armored_public_keys)
print(ascii_armored_private_keys)

public = open("public.pem", "w")
public.write(ascii_armored_public_keys)
public.close()

pgp.send_keys(
    ''.join(keyserver),
    str(key)
)

f = open("Alice", "w")
f.write("id: " + str(id) + '\n')
f.write("key id: " + str(key) + '\n')
f.write("passphrase: " + str(passphrase))

print(len(pgp.list_keys()))
#system("gpg --send-keys --user {} --keyserver keyserver.ubuntu.com {}".format(id, key))
#system("gpg --keyserver keyserver.ubuntu.com --recv-keys {}".format(key))
