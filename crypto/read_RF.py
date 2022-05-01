
Rx = 'Rx.txt'
Tx = 'Tx.txt'
radio_transmission = open(Rx, 'r')
flag = False

with open('plain.txt', 'w') as f:
    for line in radio_transmission:
        if line.strip().endswith('###end'):
            flag=False
            break
        if flag:
            print("here")
            print(line)
            f.write(line)
        if line.startswith('###start'):
            flag=True