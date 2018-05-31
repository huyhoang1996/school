import socket
import sys

# Create a TCP/IP socket
sock = socket.socket()
# Bind the socket to the port
server_address = ('localhost', 9000)
print ('starting up on %s port %s' % server_address)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    connection, client_address = sock.accept()
    try:

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(255)
            print ('received "%s"' % data)
            if not data:
                break
            
    finally:
        # Clean up the connection
        print("close server")
        connection.close()


