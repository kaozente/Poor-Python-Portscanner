import struct

class psTcpPacket:

	def __init__(self):
		pass

	def loadValuesFromRaw(self, data):
		# H = unsigned short; I = unsigned int; ! = network/big endian
		(self.srcport, self.dstport, self.seqno, self.ackno) = struct.unpack('!HHII', data[0:12])

		# flags
		


	def printList(self):
		print ("")
		print ("="*14 + " TCP " + "="*15)

		print ("Source Port: " + str(self.srcport))
		print ("Destn. Port: " + str(self.dstport))
		print ("Sequence Nr: " + str(self.seqno))
		print ("ACK Nr: " + str(self.ackno))

		print ("="*34)
		print ("")
