import gnupg
pgp = gnupg.GPG()

read_bob = open('Bob', 'r')
id = read_bob.readlines()[0].replace("id: ", '')
keyserver = 'keyserver.ubuntu.com'
read_bob.close()

print(id)

keylist = pgp.search_keys(
    ''.join(id),
    ''.join(keyserver)
)

write_bob = open('Bob', 'a')
relevant_key_index = len(keylist)-1

recv_bob = pgp.recv_keys(
    keylist[relevant_key_index]['keyid']
)
print(recv_bob)
key_bob = pgp.recv_keys(keylist[0]['keyid'])
write_bob.write(keylist[len(keylist)-1]['keyid'])
