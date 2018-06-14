import socket
import sys

sock = socket.socket()
server_address = ('localhost', 9000)
print ('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1)
while True:
    connection, client_address = sock.accept()
    try:
        while True:
            data = connection.recv(255)
            print ('received "%s"' % data)
            if not data:
                break
            
    finally:
        print("close server")
        connection.close()


