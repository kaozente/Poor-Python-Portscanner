import socket
from struct import pack

srv = socket.socket(socket.AF_INET, socket.SOCK_RAW, 0)
# Include IP headers
srv.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# create ip packet
ihlver = (4 << 4) + 5
dst = socket.inet_aton('1.1.1.1')
src = socket.inet_aton('192.168.178.62')

ip_header = pack('!BBHHHBBH4s4s' , ihlver, 0, 0,12345, 0, 255, 6, 0, src, dst)

# tcp header fields
tcp_source = 1234   # source port
tcp_dest = 80   # destination port
tcp_seq = 454
tcp_ack_seq = 0
tcp_doff = 5    #4 bit field, size of tcp header, 5 * 4 = 20 bytes
#tcp flags
tcp_fin = 0
tcp_syn = 1
tcp_rst = 0
tcp_psh = 0
tcp_ack = 0
tcp_urg = 0
tcp_window = socket.htons (5840)    #   maximum allowed window size
tcp_check = 0
tcp_urg_ptr = 0
 
tcp_offset_res = (tcp_doff << 4) + 0
tcp_flags = tcp_fin + (tcp_syn << 1) + (tcp_rst << 2) + (tcp_psh <<3) + (tcp_ack << 4) + (tcp_urg << 5)
 
# the ! in the pack format string means network order
tcp_header = pack('!HHLLBBHHH' , tcp_source, tcp_dest, tcp_seq, tcp_ack_seq, tcp_offset_res, tcp_flags,  tcp_window, tcp_check, tcp_urg_ptr)

pck = ip_header + tcp_header + 'moo'

print(list(pck))

for i in range(10):
	print("send no " + str(i))
	srv.sendto(pck, ('192.168.178.62',0))