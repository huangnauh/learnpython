import asynchat,asyncore,socket,select,urllib,SimpleHTTPServer
import os,traceback,shutil,cStringIO,cgi,sys,posixpath


class AsyncSimpleHTTPServer(asyncore.dispatcher):
    def __init__(self,address,RequestHandlerClass):
        self.address = address
        self.RequestHandlerClass = RequestHandlerClass
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(self.address)
        self.listen(5)
        
    def handle_accept(self):
        try:
            conn,addr = self.accept()
        except socket.error:
            self.log_info ('warning: server accept() threw an exception', 'warning')
            return
        self.RequestHandlerClass(conn,addr,self)


class AsyncSimpleHTTPRequestHandler(asynchat.async_chat,SimpleHTTPServer.SimpleHTTPRequestHandler):
    def __init__(self,conn,addr,server):
        self.request = conn
        self.address = addr
        self.server = server
        asynchat.async_chat.__init__(self)
        self.set_terminator('\r\n\r\n')
        self.rfile = cStringIO.StringIO()
        self.wfile = self
        self.found_terminator = self.handle_request_line
        self.request_version = "HTTP/1.1"
        
    def collect_incoming_data(self,data):
        self.rfile.write(data)
    
    def handle_request_line(self):
        self.rfile.seek(0)
        self.raw_requestline = self.rfile.readline()
        self.parse_request()
        if self.command in ['GET','HEAD']:
            mname = "do_"+self.command
            if hasattr(self,mname):
                method = getattr(self, mname)
                method()
                self.finish()
            elif self.command=="POST":
                self.prepare_POST()
            else:
                self.send_error(501, "Unsupported method (%s)" %self.command)
    
    def prepare_POST(self):
        bytesToRead = int(self.headers.getheader('content-length'))
        self.set_terminator(bytesToRead)
        self.rfile = cStringIO.StringIO()
        self.found_terminator = self.handle_post_data
        
    def handle_post_data(self):
        self.rfile.seek(0)
        self.do_POST()
    
    def do_GET(self):
        """Serve a GET request."""
        self.body = {}
        self.handle_data()
            
    def do_POST(self):
        ctype,pdict = cgi.parse_header(self.headers.getheader('content-type'))
        self.body = cgi.FieldStorage(fp=self.rfile,
            headers=self.headers, environ = {'REQUEST_METHOD':'POST'},
            keep_blank_values = 1)
        self.handle_data()
            
    def handle_data(self):
        f = self.send_head()
        if f:
            self.copyfile(f, self.wfile)
            f.close()
            
    def copyfile(self, source, outputfile):
        """Copy all data between two file objects
        Set a big buffer size"""
        shutil.copyfileobj(source, outputfile, length = 128*1024)
    
    def end_headers(self):
        if self.request_version != 'HTTP/0.9':
            self.wfile.write("\r\n")

    def write(self, data):
        self.push(data)
        
    def flush(self):
        pass
        
    
        
    
        
            
        
        
        
        
    