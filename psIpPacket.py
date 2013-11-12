class psIpPacket:
	'''
	Provides settors/gettors for comfortable creation / reading of 
	IPv4 packets
	'''

	data = 0;

	def __init__(self):
		pass		


	def loadValuesFromRaw(self, data):

		self.data = data

		# field 1 (Version / Header Lenght as VVVVIIII)
		self.ipVersion = self.data[0] >> 4
		self.ipIHL = self.data[0] & 0b00001111

		#field 2 (DSSP / ECN as DDDDDDEE)
		# ignore

		#field 3/4 (Packet Length)
		self.PLength = (self.data[2] << 8) + self.data[3]

		#field 5/6 (Packet ID)
		self.PID = (self.data[4] << 8) + self.data[5]

		#field 7 (Flags R/MF/DF / Fragment Offset)
		# ignore

		#field 8 (TTL)
		# ignore

		#field 9 (Protocol; TCP == 6))
		self.proto = (self.data[9])

		#field10/11 (Header Checksum)
		self.checksum = (self.data[10] << 8) + self.data[11]

		#field12-15 (Source IP Addr)
		self.src  = str(self.data[12])
		self.src += "."
		self.src += str(self.data[13])
		self.src += "."
		self.src += str(self.data[14])
		self.src += "."
		self.src += str(self.data[15])

		#field16-19 (Dest. IP Addr)
		self.dst  = str(self.data[16])
		self.dst += "."
		self.dst += str(self.data[17])
		self.dst += "."
		self.dst += str(self.data[18])
		self.dst += "."
		self.dst += str(self.data[19])



	def printList(self):
		print ("")
		print ("="*15 + " IP " + "="*15)

		print ("Source Addr: " + self.src)
		print ("Destn. Addr: " + self.dst)
		print ("Version: " + str(self.ipVersion)),
		print ("IHL: " + str(self.ipIHL))
		print ("Total Length of Packet: " + str(self.PLength))
		print ("Packet Ident: " + str(self.PID))
		print ("Protocol Nr: " + str(self.proto))
		print ("Checksum: " + str(hex(self.checksum)))

		print ("="*34)
		print ("")


