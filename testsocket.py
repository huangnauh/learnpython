import socketserver
import socket
import select

def _eintr_retry(func, *args):
    """restart a system call interrupted by EINTR"""
    while True:
        try:
            return func(*args)
        except OSError as e:
            if e.errno != errno.EINTR:
                raise
class BaseServer:
    timeout = None

    def __init__(self, server_address, RequestHandlerClass):
        """Constructor.  May be extended, do not override."""
        self.server_address = server_address
        self.RequestHandlerClass = RequestHandlerClass
        self.__is_shut_down = threading.Event()
        self.__shutdown_request = False

    def server_activate(self):
        """Called by constructor to activate the server.

        May be overridden.

        """
        pass

    def serve_forever(self, poll_interval=0.5):
        """Handle one request at a time until shutdown.

        Polls for shutdown every poll_interval seconds. Ignores
        self.timeout. If you need to do periodic tasks, do them in
        another thread.
        """
        self.__is_shut_down.clear()
        try:
            while not self.__shutdown_request:
                # XXX: Consider using another file descriptor or
                # connecting to the socket to wake this up instead of
                # polling. Polling reduces our responsiveness to a
                # shutdown request and wastes cpu at all other times.
                r, w, e = _eintr_retry(select.select, [self], [], [],
                                       poll_interval)
                if self in r:
                    self._handle_request_noblock()

                self.service_actions()
        finally:
            self.__shutdown_request = False
            self.__is_shut_down.set()

    def shutdown(self):
        """Stops the serve_forever loop.

        Blocks until the loop has finished. This must be called while
        serve_forever() is running in another thread, or it will
        deadlock.
        """
        self.__shutdown_request = True
        self.__is_shut_down.wait()

    def service_actions(self):
        """Called by the serve_forever() loop.

        May be overridden by a subclass / Mixin to implement any code that
        needs to be run during the loop.
        """
        pass

    def handle_request(self):
        """Handle one request, possibly blocking.

        Respects self.timeout.
        """
        # Support people who used socket.settimeout() to escape
        # handle_request before self.timeout was available.
        timeout = self.socket.gettimeout()
        if timeout is None:
            timeout = self.timeout
        elif self.timeout is not None:
            timeout = min(timeout, self.timeout)
        fd_sets = _eintr_retry(select.select, [self], [], [], timeout)
        if not fd_sets[0]:
            self.handle_timeout()
            return
        self._handle_request_noblock()

    def _handle_request_noblock(self):

        try:
            request, client_address = self.get_request()
        except OSError:
            return
        if self.verify_request(request, client_address):
            try:
                self.process_request(request, client_address)
            except:
                self.handle_error(request, client_address)
                self.shutdown_request(request)

    def handle_timeout(self):
        pass

    def verify_request(self, request, client_address):
        return True

    def process_request(self, request, client_address):
        self.finish_request(request, client_address)
        self.shutdown_request(request)

    def server_close(self):
        pass

    def finish_request(self, request, client_address):
        """Finish one request by instantiating RequestHandlerClass."""
        self.RequestHandlerClass(request, client_address, self)

    def shutdown_request(self, request):
        """Called to shutdown and close an individual request."""
        self.close_request(request)

    def close_request(self, request):
        """Called to clean up an individual request."""
        pass

    def handle_error(self, request, client_address):
        print('-'*40)
        print('Exception happened during processing of request from', end=' ')
        print(client_address)
        import traceback
        traceback.print_exc() # XXX But this goes to stderr!
        print('-'*40)


class TCPServer(BaseServer):

    address_family = socket.AF_INET

    socket_type = socket.SOCK_STREAM

    request_queue_size = 5

    allow_reuse_address = False

    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
        """Constructor.  May be extended, do not override."""
        BaseServer.__init__(self, server_address, RequestHandlerClass)
        self.socket = socket.socket(self.address_family,
                                    self.socket_type)
        if bind_and_activate:
            self.server_bind()
            self.server_activate()

    def server_bind(self):
        """Called by constructor to bind the socket.

        May be overridden.

        """
        if self.allow_reuse_address:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)
        self.server_address = self.socket.getsockname()

    def server_activate(self):
        """Called by constructor to activate the server.

        May be overridden.

        """
        self.socket.listen(self.request_queue_size)

    def server_close(self):
        """Called to clean-up the server.

        May be overridden.

        """
        self.socket.close()

    def fileno(self):
        """Return socket file number.

        Interface required by select().

        """
        return self.socket.fileno()

    def get_request(self):
        """Get the request and client address from the socket.

        May be overridden.

        """
        return self.socket.accept()

    def shutdown_request(self, request):
        """Called to shutdown and close an individual request."""
        try:
            #explicitly shutdown.  socket.close() merely releases
            #the socket and waits for GC to perform the actual close.
            request.shutdown(socket.SHUT_WR)
        except OSError:
            pass #some platforms may raise ENOTCONN here
        self.close_request(request)

    def close_request(self, request):
        """Called to clean up an individual request."""
        request.close()

class BaseRequestHandler:
    def __init__(self, request, client_address, server):
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

    """Define self.rfile and self.wfile for stream sockets."""

    # Default buffer sizes for rfile, wfile.
    # We default rfile to buffered because otherwise it could be
    # really slow for large data (a getc() call per byte); we make
    # wfile unbuffered because (a) often after a write() we want to
    # read and we need to flush the line; (b) big writes to unbuffered
    # files are typically optimized by stdio even when big reads
    # aren't.
    rbufsize = -1
    wbufsize = 0

    # A timeout to apply to the request socket, if not None.
    timeout = None

    # Disable nagle algorithm for this socket, if True.
    # Use only when wbufsize != 0, to avoid small packets.
    disable_nagle_algorithm = False

    def setup(self):
        self.connection = self.request
        if self.timeout is not None:
            self.connection.settimeout(self.timeout)
        if self.disable_nagle_algorithm:
            self.connection.setsockopt(socket.IPPROTO_TCP,
                                       socket.TCP_NODELAY, True)
        self.rfile = self.connection.makefile('rb', self.rbufsize)
        self.wfile = self.connection.makefile('wb', self.wbufsize)

    def finish(self):
        if not self.wfile.closed:
            try:
                self.wfile.flush()
            except socket.error:
                # An final socket error may have occurred here, such as
                # the local error ECONNABORTED.
                pass
        self.wfile.close()
        self.rfile.close()
		

class MyTCPHandler(socketserver.BaseRequestHandler):
	def handle(self):
		self.data = self.request.recv(1024).strip()
		print("{} wrote:".format(self.client_address[0]))
		print(self.data)
		self.request.sendall(self.data.upper())

class MyTCPHandler1(socketserver.StreamRequestHandler):
	def handle(self):
		self.data = self.rfile.readline().strip()
		print("{} wrote:".format(self.client_address[0]))
		print(self.data)
		self.wfile.write(self.data.upper())
		
if __name__ == "__main__":
	HOST, PORT = "localhost",9999
	server = socketserver.TCPServer((HOST,PORT),MyTCPHandler)
	server.serve_forever()
	