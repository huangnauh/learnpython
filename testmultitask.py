from contextlib import closing
import socket
import multitask
def client_handler(sock):
	with closing(sock):
		while 1:
			try:
				data = (yield multitask.recv(sock,1024))
			except socket.error,e:
				print "****",e
				raise
			print "recv:",data
			if not data:
				break
			data += "...OK"
			yield multitask.send(sock,data)
			print "send:",data

def echo_server(hostname,port):
	addrinfo = socket.getaddrinfo(hostname,port,socket.AF_UNSPEC,socket.SOCK_STREAM)
	(family,socktype,proto,canonname,sockaddr) = addrinfo[0]
	print (family,socktype,proto,canonname,sockaddr)
	with closing(socket.socket(family,socktype,proto)) as sock:
	#with closing(socket.socket(socket.AF_INET,socket.SOCK_STREAM)) as sock:
		sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		sock.bind(sockaddr)
		#sock.bind((hostname,port))
		sock.listen(5)
		print sockaddr
		while 1:
			multitask.add(client_handler((yield multitask.accept(sock))[0]))

if __name__ == "__main__":
	import sys
	hostname = '127.0.0.1'
	port = 1234
	multitask.add(echo_server(hostname,port))
	try:
		multitask.run()
	except KeyboardInterrupt:
		pass
	except socket.error,e:
		print "rrrrr",e

		