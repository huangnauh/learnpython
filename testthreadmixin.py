import socket
import threading
import socketserver

class BaseRequestHandler:
    def __init__(self,request,client_address,server):
        self.request = request
        self.client_address = client_address
        self.server = server
        self.setup()
        try:
            self.handle()
        finally:
            self.finish()
    def setup(self):
        pass
    def handle(self):
        pass
    def finish(self):
        pass

class StreamRequestHandler(BaseRequestHandler):
    rbufsize = -1
    wbufsize = 0
    timeout = None
    disable_nagle_algorithm = False
    def setup(self):
        self.conn = self.request
        if self.timeout is not None:
            self.conn.settimeout(self.timeout)
        if self.disable_nagle_algorithm:
            self.conn.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True)
        self.rfile = self.conn.makefile('rb',-1)
        self.wfile = self.conn.makefile('wb',0)
    def finish(self):
        if not self.wfile.close():
            try:
                self.wfile.flush()
            except socket.error:
                pass
        self.wfile.close()
        self.read.close()
        
        
        
class TCPServer:
	address_family = socket.AF_INET
	socket_type = socket.SOCK_STREAM
	allow_reuse_address = False
	request_queue_size = 5
	def __init__(self,server_address,RequestHandlerClass,bind_and_active=True):
		self.server_address = server_address
		self.RequestHandlerClass = RequestHandlerClass
		self._is_shut_down = threading.Event()
		self._shutdown_request = False
		self.socket = socket.socket(self.address_family,self.socket_type)
		if bind_and_active:
			self.server_bind()
			self.server_active()
	def server_bind(self):
		if self.allow_reuse_address:
			self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		self.socket.bind(self.server_address)
		self.server_address = self.socket.getsockname()
	def server_active(self):
		self.socket.listen(self.request_queue_size)
	def fileno(self):
		return self.socket.fileno()
	def serve_forever(self,poll_interval=0.5):
		self._is_shut_down.clear()
		try:
			while not self._shutdown_request:
				r,w,e = _eintr_retry(select.select,[self],[],[],poll_interval)
				if self in r:
					self._handle_request_noblock()
				self.service_actions()
		finally:
			self._shutdown_request = False
			self._is_shut_down.set()
	def _handle_request_noblock(self):
		try:
			request, client_address= self.get_request()
		except OSError:
			return
		try:
			self.process_request(request,client_address)
		except:
			self.handle_error(request,client_address)
			self.shutdown_request(request)
	def get_request(self):
		return self.socket.accept()
	def process_request(self,request,client_address):
		self.finish_request(request,client_address)
		self.shutdown_request(request)
	def finish_request(self,request,client_address):
		self.RequestHandlerClass(request,client_address,self)
	def shutdown_request(self,request):
		try:
			request.shutdown(socket.SHUT_WR)
		except OSError:
			pass
		request.close()
	def handle_error(request,client_address):
		print('-'*40)
		print('Exception happened during processing of request from', end=' ')
		print(client_address)
		import traceback
		traceback.print_exc()
		print('-'*40)
        
class ForkingMixIn:
    timeout = 
    active_children = None
    max_children = 40
    def collect_children(self):
        if not self.active_children:
            return
        while len(self.active_children) >= self.max_children:
            try:
                pid,_ = os.waitpid(-1,0)
                self.active_children.discard(pid)
            except InterruptedError:
                pass
            except ChildrenProcessError:
                self.active_children.clear()
            except OSError:
                break
        for pid in self.active_children.copy():
            try:
                pid,_ = os.waitpid(pid,os.WNOHANG)
                self.active_children.discard(pid)
            except ChildrenProcessError:
                self.active_children.discard(pid)
            except OSError:
                pass
                
    def handle_timeout(self):
        self.collect_children()
        
    def service_action(self):
        self.collect_children()
    def process_request(self,request,client_address):
        pid = os.fork()
        if pid:
            if self.active_children is None:
                self.active_children = set()
            self.active_children.add(pid)
            self.close_request(request)
            return
        else:
            try:
                self.finish_request(request,client_address)
                self.shutdown_request(request)
                os._exit(0)
            except:
                try:
                    self.handle_error(request,client_address)
                    self.shutdown_request(request)
                finally:
                    os._exit(1)
            
            
class ThreadingMixIn:
	daemon_threads = False
	def process_request(self,request,client_address):
		print(type(client_address),' ',client_address)
		t = threading.Thread(
			target=self.process_request_thread,
			args = (request,client_address))
		t.daemon = self.daemon_threads
		t.start()
	def process_request_thread(self,request,client_address):
		try:
			self.finish_request(request,client_address)
			self.shutdown_request(request)
		except:
			self.handle_error(request,client_address)
			self.shutdown_request(request)
			
class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        cur_thread = threading.current_thread()
        response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
        self.request.sendall(response)

class ThreadedTCPServer(ThreadingMixIn, socketserver.TCPServer):
    pass

def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))
    finally:
        sock.close()

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 0

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)

    client(ip, port, "Hello World 1")
    client(ip, port, "Hello World 2")
    client(ip, port, "Hello World 3")

    server.shutdown()