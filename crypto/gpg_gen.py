import random
import string
import gnupg
pgp = gnupg.GPG()
from os import system

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


for i in range(0,10):
    print(gen_id(emails))
    print(gen_passhphrase())

id = gen_id(emails)
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
key = pgp.gen_key(input_data)
print(key)

# create ascii-readable versions of pub / private keys
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


# encrypt
with open('plain.txt', 'rb') as f:
    status = pgp.encrypt_file(
        file=f,
        recipients=['W5Yalr2lmX@outlook.com'],
        output='encrypted.txt.gpg',
    )
# decrypt
with open('encrypted.txt.gpg', 'rb') as f:
    status = pgp.decrypt_file(
        file=f,
        passphrase='zrPROvlBefcCGXpuXuskTpSLfwpPrnlwyYzJAdrmmPZhRvPF',
        output='decrypted.txt',
    )


pgp.send_keys(
    ''.join(keyserver),
    str(key)
)

keylist = pgp.search_keys(
    "a04GdjLV@godaddy.com",
    "keyserver.ubuntu.com"
)

key_b = pgp.recv_keys(keylist[0]['keyid'])

#system("gpg --send-keys --user {} --keyserver keyserver.ubuntu.com {}".format(id, key))
#system("gpg --keyserver keyserver.ubuntu.com --recv-keys {}".format(key))