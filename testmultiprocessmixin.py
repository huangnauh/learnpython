import socket
def client(ip,port,message):
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.connect((ip,port))
	try:
		sock.sendall(bytes(message,'ascii'))
		response = str(sock.recv(1024),'ascii')
		print("Receive:{}".format(response))
	finally:
		sock.close()
if __name__ == '__main__':
	ip,port = '127.0.0.1',5000
	client(ip, port, "Hello World 1")
	client(ip, port, "Hello World 2")
	client(ip, port, "Hello World 3")