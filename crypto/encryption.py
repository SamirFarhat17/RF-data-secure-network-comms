import gnupg
pgp = gnupg.GPG()

counterpart = open('Bob', 'r')

id = counterpart.readlines()[0].replace("key id: ", '')
id = id.replace('\n', '')
print(id)

# encrypt
with open('plain.txt', 'rb') as f:
    status = pgp.encrypt_file(
        file=f,
        recipients=id,
        output='encrypted.txt.gpg',
    )
print('ok: ', status.ok)
print('status: ', status.status)
print('stderr: ', status.stderr)
