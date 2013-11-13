import socket
from struct import pack
s = socket.socket(socket.AF_INET, socket.SOCK_RAW)


source_ip = '192.168.178.62'
dest_ip = '1.1.1.1'

ip_saddr = socket.inet_aton ( source_ip )  
ip_daddr = socket.inet_aton ( dest_ip )

for i in range(255):
	ip_header = pack('!BBHHHBBH4s4s' , 69, 0, 20, 12345, 2, 77, i, 0, ip_saddr, ip_daddr)
	s.sendto(ip_header, ('2.2.2.2', 0))