import sys
import socket

version = '0.0.1'
usage = 'usage: ' + sys.argv[0] + ' connect|syn host port [portrange]'

print ('Der Geile Portscanner v ' + version)


if len(sys.argv) < 1:
	#usage = sys.argv[1]
	usage = 'bla bla usage'
	print (usage)


print (usage)