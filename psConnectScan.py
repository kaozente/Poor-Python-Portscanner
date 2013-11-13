import socket

def connectScanPort(host, port):
	# AF_INET -> IPv4
	# SOCK_STREAM -> TCP-Style
	print ("Scanning Port " + str(port)),
	sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		sck.connect((host, port))
		# if this doesn't fail, the port is open
		sck.close
		print (" - OPEN!")
	except socket.error as err:
		print (" - closed.")
		#print (err)