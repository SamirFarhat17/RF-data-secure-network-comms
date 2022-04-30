import gnupg
pgp = gnupg.GPG()

counterpart = open('Bob', 'r')

id = counterpart.readlines()[0].replace("id: ", '')
id = id.replace('\n', '')
print(id)

# encrypt
with open('plain.txt', 'rb') as f:
    status = pgp.encrypt_file(
        file=f,
        recipients=[''.join(id)],
        output='encrypted.txt.gpg',
    )