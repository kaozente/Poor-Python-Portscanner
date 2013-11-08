'''
Run a Server that prints all raw packets coming in
on a specified port (defaults to 1337)
'''

import socket
import sys
import struct

# so und nicht anders
host = '127.0.0.1'
port = 1337

try:
	# socket creation: 
	# AF_INET --> IPv4 Address
	# SOCK_RAW --> Raw socket
	# IPPROTO_IP --> Scan on TCP basis
	srv = socket.socket(socket.AF_INET, socket.SOCK_RAW, 0)

	# Bind to 0.0.0.0 (all avaiblable IPs) and listen (max 1 connection)
	srv.bind((host, port))
	#srv.listen(1)

except socket.error as (errno, errmsg):
	print "Error while creating socket:"
	print errmsg + " (" + str(errno) + ")"
	sys.exit()

print "weeeeeeeeeeeeeeey running!"
print (srv.getsockname())

str = srv.recv(128)
print "Received:"
print (str)
print "Hexdump:"
print (struct.unpack(str))

'''
clisock, (remhost, remport) = srv.accept()
print "Connection from " + remhost
str = clisock.recv(100)
print (str)
clisock.close()
'''