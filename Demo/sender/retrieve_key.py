import gnupg
from nbformat import write
pgp = gnupg.GPG()
from os import system

print(len(pgp.list_keys()))
read_bob = open('Bob', 'r')
id = read_bob.readlines()[0].replace("id: ", '')
id.replace('\n', '')
read_bob.close()

keyserver = 'keyserver.ubuntu.com'
print(id)

keylist = pgp.search_keys(
    ''.join(id),
    ''.join(keyserver)
)

recv_bob = pgp.recv_keys(
        'keyserver.ubuntu.com', 
        ''.join(keylist[len(keylist)-1]['keyid'])
)
print(keylist[len(keylist)-1]['keyid'])

print(keylist)
write_bob = open('Bob', 'w')
write_bob.write(id)
write_bob.write(keylist[len(keylist)-1]['keyid'])

ascii_armored_public_keys = pgp.export_keys(keylist[0]['keyid'])
with open('bob_pub.pem', 'w') as f:
    f.write(ascii_armored_public_keys)


key_bob = pgp.recv_keys(keylist[0]['keyid'])
export_result = pgp.export_keys(keylist[len(keylist)-1]['keyid'])

print(len(pgp.list_keys()))
#system("gpg --export --armor {} | sudo apt-key add - && sudo apt-get update".format(keylist[0]['fingerprint']))
#system("gpg --edit-key {}".format(keylist[len(keylist)-1]['keyid']))
my_key_list = pgp.list_keys()
print(my_key_list[len(my_key_list)-1])
fingerprint = my_key_list[len(my_key_list)-1]['fingerprint']
print(fingerprint)
pgp.trust_keys(fingerprint, "TRUST_ULTIMATE")