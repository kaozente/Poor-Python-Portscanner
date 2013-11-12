'''
Run a Server that prints all raw packets coming in
on a specified port (defaults to 1337)
'''

import socket
import sys

from psIpPacket import psIpPacket
from psTcpPacket import psTcpPacket

# so und nicht anders
host = '127.0.0.1'
port = 1337

#print(sys.version_info)


try:
	# socket creation: 
	# AF_INET --> IPv4 Address
	# SOCK_RAW --> Raw socket
	# IPPROTO_IP --> Scan on TCP basis
	srv = socket.socket(socket.AF_INET, socket.SOCK_RAW, 0)

	# Bind to 0.0.0.0 (all avaiblable IPs) and listen (max 1 connection)
	srv.bind((host, port))
	#srv.listen(1)

#except socket.error as (errno, errmsg):
except socket.error as errmsg:
	print ("Error while creating socket:")
	print (errmsg)
	#+ " (" + str(errno) + ")"
	sys.exit()

print ("weeeeeeeeeeeeeeey running!")
print (srv.getsockname())

try:
	data = srv.recv(128)
	print ("Received:")
	print (data)
	print (list(data))

	# Analyze IP Header
	ip_data = data[0:20]
	pck = psIpPacket()
	pck.loadValuesFromRaw(ip_data)
	pck.printList()

	# Is it TCP?
	if pck.proto == 6:
		print ("It's TCP yeah!")
		tcp_data = data[20:39]
		print(list(tcp_data))
		tcppck = psTcpPacket()
		tcppck.loadValuesFromRaw(tcp_data)
		tcppck.printList()


	#print ("Hexdump:")
	#print (struct.unpack(str))
except KeyboardInterrupt:
	print ("Exit by KeyboardInterrupt")

print ("Exit 0")

'''
clisock, (remhost, remport) = srv.accept()
print "Connection from " + remhost
str = clisock.recv(100)
print (str)
clisock.close()
'''