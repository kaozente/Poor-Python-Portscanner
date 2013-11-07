'''
Run a Server that prints all raw packets coming in
on a specified port (defaults to 1337)
'''

import socket

port = 1337


srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(('', port))
srv.listen(1)

print "weeeeeeeeeeeeeeey running!"
print (srv.getsockname())


clisock, (remhost, remport) = srv.accept()
print "Connection from " + remhost
str = clisock.recv(100)
print (str)
clisock.close()