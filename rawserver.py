'''
Run a Server that prints all raw packets coming in
on a specified port (defaults to 1337)
'''

import socket
import sys

from psIpPacket import psIpPacket
from psTcpPacket import psTcpPacket


# so und nicht anders
host = '0.0.0.0'
port = 1337

#print(sys.version_info)


try:
	# socket creation: 
	# AF_INET --> IPv4 Address
	# SOCK_RAW --> Raw socket
	# IPPROTO_IP --> Scan on TCP basis
	srv = socket.socket(socket.AF_INET, socket.SOCK_RAW, 0)
	srv.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

	# Bind to 0.0.0.0 (all avaiblable IPs) and listen (max 1 connection)
	srv.bind((host, 0))
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
	while 1:
		data = srv.recv(4096)
		print ("Received:")
		#print (data)
		#print (list(data))

		# Analyze IP Header
		ip_data = data[0:20]
		pck = psIpPacket()
		pck.loadValuesFromRaw(ip_data)
		pck.printList()

		# Is it TCP?
		if pck.proto == 6:
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