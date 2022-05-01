import gnupg
pgp = gnupg.GPG()
from os import system

read_bob = open('Bob', 'r')
id = read_bob.readlines()[0].replace("id: ", '')
keyserver = 'keyserver.ubuntu.com'
read_bob.close()

print(id)

keylist = pgp.search_keys(
    ''.join(id),
    ''.join(keyserver)
)
print(keylist)
write_bob = open('Bob', 'a')
relevant_key_index = len(keylist)-1

print(pgp.list_keys())

recv_bob = pgp.recv_keys(
        'keyserver.ubuntu.com', 
        ''.join(keylist[relevant_key_index]['keyid'])
)
print(''.join(keylist[relevant_key_index]['keyid']))
print(pgp.list_keys())

key_bob = pgp.recv_keys(keylist[0]['keyid'])
write_bob.write(keylist[len(keylist)-1]['keyid'])
print(keylist[0]['keyid'])
#export_result = pgp.export_keys(keylist[relevant_key_index]['keyid'])
system("gpg --export --armor {} | sudo apt-key add - && sudo apt-get update".format(keylist[0]['keyid']))
