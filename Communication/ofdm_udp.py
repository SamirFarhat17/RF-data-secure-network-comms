import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 50001
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(0.5)
while True:
    try:
        data, addr = sock.recvfrom(128) 
        print("Msg:", data, 'Hex:', ' '.join('{:02x}'.format(x) for x in data))
    except socket.timeout:
        pass