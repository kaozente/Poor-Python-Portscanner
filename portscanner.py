'''
Scan one or more ports using one of the two modes:

 Connect Scan: try establishing a TCP Connection. If it
 	suceeds, the port is open. If the host refuses the
 	connection or timeout is reached, the port is closed.

 Syn Scan: manually create a TCP syn packet. Then sniff all
 	incoming packets using a raw socket. Check all of them
 	to find TCP packets that are in response to the sent one.
 	If it's a SYN ACK packet, the port is open. If no response
 	packet is received, the port is closed.

Built and tested using Python 3.3.2 on Windows 7.
I found during development that RAW Sockets are highly 
different on different OS, and error catching is not really
implementet here, so the script crashing is probably because
it received answers from the raw socket that were different 
from the expected Win7 behaviour.

Also, this script must be executed as ADMIN!
'''

import sys
import socket
from psConnectScan import connectScanPort
from psSynScan import synScanPort

version = '0.0.1'
usage = 'usage: ' + sys.argv[0] + ' connect|syn host port [portrange]'

print ('ISEC Python Portscanner v ' + version)
print ("-"*40)


if len(sys.argv) < 4:
	print (usage)
	sys.exit()

(mode, host) = sys.argv[1:3]
port = int(sys.argv[3])
print("Getting IP for host " + host + "...")
ip = socket.gethostbyname(host)


print("Timeout:" + str(socket.getdefaulttimeout()))

print("Scanning Host " + str(host) + " / " + str(ip))

try:
	if len(sys.argv) > 4:
		endport = int(sys.argv[4])
		total = endport - port + 1
		print("Range Scan Mode! Will scan port " + str(port) + " to " + str(endport))
		print("Scanning " + str(total) + " ports. This may take a while.")
		print("-"*40)
		for port in range(port, (endport+1)):
			connectScanPort(ip, port)
	else:
		print("Single Port Scan Mode.")
		print("-"*40)
		connectScanPort(ip, port)
except KeyboardInterrupt:
	print ("Exit by KeyboardInterrupt")


