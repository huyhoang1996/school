import socket, sys
from struct import *
from datetime import datetime 
import os


#create an INET, STREAMing socket to detect network traffic packet
# INET (i.e. IPv4) sockets
# SOCK_RAW to raw data
# IPPROTO_TCP or IPPROTO_UDP
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
except socket.error:
    print ('Socket could not be created. Error Code SOCK_RAW: ')
    sys.exit()

result = '' 
data_return = ''
# receive a packet
# os.system("python server.py &")
# os.system("python client.py a")

def process():
    count = 0
    global result
    global data_return
    result = '' 
    while True:
        packet = s.recvfrom(65565)
         
        #packet string from tuple
        packet = packet[0]
         
        #take first 20 characters for the ip header
        ip_header = packet[0:20]
         
        #now unpack them 
        iph = unpack('!BBHHHBBH4s4s' , ip_header)
         
        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF
         
        iph_length = ihl * 4
         
        ttl = iph[5]
        protocol = iph[6]
        s_addr = socket.inet_ntoa(iph[8]);
        d_addr = socket.inet_ntoa(iph[9]);
         
        result+= '\n'+'Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)
         
        tcp_header = packet[iph_length:iph_length+20]
         
        #now unpack them 
        tcph = unpack('!HHLLBBHHH' , tcp_header)
         
        source_port = tcph[0]
        dest_port = tcph[1]
        sequence = tcph[2]
        acknowledgement = tcph[3]
        doff_reserved = tcph[4]
        tcph_length = doff_reserved >> 4
         
        result+= '\n'+ 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length)
         
        h_size = iph_length + tcph_length * 4
        data_size = len(packet) - h_size
         
        #get data from the packet
        data = packet[h_size:]
         
        result+= '\n'+'Data : ' + str(data)
        result+='\n'

        if len(str(data)) > 4:
            break;
        else:
            result = ''
    return result


