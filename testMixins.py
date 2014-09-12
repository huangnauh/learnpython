import socket
import multiprocessing as mp
import socketserver

class MultiprocessTCPRequestHandler(socketserver.BaseRequestHandler):
	def handle(self):
		data = str(self.request.recv(1024),'ascii')
		cur_process = mp.current_process()
		response = bytes("{}:{}".format(cur_process.name,data),'ascii')
		self.request.sendall(response)
		
class MultiprocessingMixIn:
	daemon_threads = False
	def process_request(self,request,client_address):
		self.request = request
		t = mp.Process(
			target=self.process_request_process,
			args = (client_address,))
		t.daemon = self.daemon_threads
		t.start()
	def process_request_process(self,client_address):
		try:
			self.finish_request(self,
					    self.request,client_address)
			self.shutdown_request(self.request)
		except:
			self.handle_error(self.request,client_address)
			self.shutdown_request(self.request)

		
class MutiProcessTCPServer(MultiprocessingMixIn,socketserver.TCPServer):
	pass
	
if __name__ == '__main__':
	Host,Port = 'localhost',5000
	server = MutiProcessTCPServer((Host,Port),MultiprocessTCPRequestHandler)
	ip,port = server.server_address
	server.serve_forever()
