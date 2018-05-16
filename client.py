
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 9000)
print 'Client connecting to %s port %s' % server_address
sock.connect(server_address)
try:
    
    # Send data
    message = 'This is the message from client'
    sock.send(message)

finally:
    print'Client closing socket'
    sock.close()

#     Traceback (most recent call last):
#   File "client.py", line 30, in <module>
#     sock.connect(server_address)
#   File "/usr/lib/python2.7/socket.py", line 228, in meth
#     return getattr(self._sock,name)(*args)
# socket.error: [Errno 111] Connection refused
