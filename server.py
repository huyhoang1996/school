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
count =0
while True:
    # Wait for a connection
    connection, client_address = sock.accept()
    try:

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(255)
            print ('received "%s"' % data)
            if data:
                count +=1
                connection.sendall("This is the message. From server. %s" % count)
            else:
                break
            
    finally:
        # Clean up the connection
        connection.close()


