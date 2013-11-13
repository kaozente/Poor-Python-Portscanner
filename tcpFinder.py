import socket
import struct

def dump(data):
	for i in data:
		print(str(ord(i))),
		print " ",
	print 

srv = socket.socket(socket.AF_INET, socket.SOCK_RAW, 0)
# Include IP headers
srv.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
#srvioctl(socket.SIO_RCVALL, socket.RCVALL_ON)


# Bind to 0.0.0.0 (all avaiblable IPs) and listen (max 1 connection)
srv.bind(('192.168.178.62', 0))

try:
	while 1:
		#print
		#print "-"*64
		data = srv.recv(4096)
		#dump(data)
		#print(str(len(data)))
		ipheader = data[0:20]
		# check  IP Header length IHL
		ipIHL = ord(ipheader[0]) & 0b00001111
		ipIHL *= 5

		ipSrc  = str(ord(ipheader[12]))
		ipSrc += "."
		ipSrc += str(ord(ipheader[13]))
		ipSrc += "."
		ipSrc += str(ord(ipheader[14]))
		ipSrc += "."
		ipSrc += str(ord(ipheader[15]))

		#check if it's TCP
		proto = (ord(ipheader[9]))
		if proto == 6:
			#print ("Received TCP Packet from "),
			print (str(ipSrc)),
			print (" Port "),
			tcpheader = data[20:40]
			#check if it's THE port!
			(srcport, dstport, seqno, ackno) = struct.unpack('!HHII', tcpheader[0:12])
			print (str(srcport)),
			print (" -> "),
			print (str(dstport)),

			flagspace = ord(tcpheader[13])
			print (" Flags "),
			print(str(flagspace)),
			print " [",

			def bitset(bm,index):
				return ((bm & 1<<index) != 0)

			print (str(seqno) + " "),

			if bitset(flagspace, 1):
				print ("SYN "),
			if bitset(flagspace, 4):
				print("ACK " + str(ackno) + " "),
			if bitset(flagspace, 2):
				print ("RST "),
			if bitset(flagspace, 0):
				print("FIN "),
			print "]"
			#dump(tcpheader)

except KeyboardInterrupt:
	print ("Exit by KeyboardInterrupt")