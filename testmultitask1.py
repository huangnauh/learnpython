import socket
from contextlib import closing

HOST = 'localhost'
PORT = 1234
ADDR = (HOST,PORT)

with closing(socket.socket(socket.AF_INET,socket.SOCK_STREAM)) as sock:
	sock.connect(ADDR)
	while 1:
		data = raw_input(">")
		if not data:
			break
		sock.send(data)
		data = sock.recv(1024)
		if not data:
			break
		print data