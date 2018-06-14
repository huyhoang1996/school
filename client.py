import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 9000)
sock.connect(server_address)
try:
    
    data = sys.argv[1:]
    message = ''
    for item in data:
        message += str(' ' + item)
    sock.sendall(message)


finally:
    sock.close()
