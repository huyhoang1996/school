import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 9000)
sock.connect(server_address)
try:
    
    # Send data
    message = 'This is the message. From client.'
    sock.sendall(message)
    
    count = 0
    while count <2:
        count+=1
        data = sock.recv(255)
        if len(data)>10:
            data = ''
            sock.sendall(message)

finally:
    sock.close()
