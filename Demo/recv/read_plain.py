Rx = 'Rx.txt'
Tx = 'Tx.txt'
radio_transmission = open(Rx, 'r')
flag = False

with open('Bob', 'w') as f:
    for line in radio_transmission.readlines():
        if line.strip().startswith('###end') and flag:
            flag=False
            break
        if flag:
            print(line)
            f.write(line)
        if line.startswith('###start'):
            flag=True
f.close()
