import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 9000)
sock.connect(server_address)
try:
    
    # Send data
    data = sys.argv[1:]
    message = ''
    for item in data:
        message += str(' ' + item)
    sock.sendall(message)


finally:
    sock.close()
