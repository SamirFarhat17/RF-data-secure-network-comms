
tx = open("Tx.txt", "w")
tx.write("###start\n")
to_send = open("Alice", "r")


for line in to_send.readlines():
    tx.write(line)

tx.write("\n###end")
tx.close()
to_send.close()
