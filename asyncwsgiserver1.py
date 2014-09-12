# encoding: utf-8


import asynchat
import asyncore
import io
import socket
import sys
import wsgiref.handlers
from wsgiref.simple_server import WSGIRequestHandler
import cgi




class AsynWsgiRequestHandler(asynchat.async_chat,WSGIRequestHandler):

    READING_HTTP_HEADER = 0
    READING_HTTP_POST_DATA = 1
    READING_DONE = 2


    def __init__(self, request, client_address, server):
        asynchat.async_chat.__init__(self, request)
        self.request = request
        self.client_address = client_address
        self.server = server
        self.rfile = io.BytesIO()
        self.post_data=io.BytesIO
        self.wfile = self
        self.set_terminator(b"\r\n\r\n")
        self.state = AsynWsgiRequestHandler.READING_HTTP_HEADER

    def collect_incoming_data(self, data):
        self.rfile.write(data)


    def found_terminator(self):
        if self.state == AsynWsgiRequestHandler.READING_HTTP_HEADER:
            self.rfile.seek(0)
            self.raw_requestline = self.rfile.readline()
            self.parse_request()
            if self.command == "POST":
                length = self.headers.getheader('content-length')
                if length:
                    self.set_terminator(content_length)
                else:
                    self.set_terminator(b"\0")
                self.state = AsynWsgiRequestHandler.READING_HTTP_POST_DATA
            else:
                self.set_terminator(None)
                self.state = AsynWsgiRequestHandler.READING_DONE
            self.rfile = io.BytesIO()
        elif self.state == AsynWsgiRequestHandler.READING_HTTP_POST_DATA:
            self.set_terminator(None)
            self.post_data=io.BytesIO(self.rfile.getvalue())
            self.rfile = io.BytesIO()
            self.state = AsynWsgiRequestHandler.READING_DONE
        if self.state == AsynWsgiRequestHandler.READING_DONE:
            errors = io.StringIO()
            handler = wsgiref.handlers.SimpleHandler(self.post_data, self.wfile, errors, self.get_environ(), False, False)
            handler.server_software = "AsyncWsgiServer Python/" + sys.version.split()[0]
            handler.run(self.server.get_app())
            if len(errors.getvalue()) != 0:
                print(errors.getvalue())
    def write(self, data):
        self.push(data)
    def flush(self):
        pass




class WsgiServer(asyncore.dispatcher):

    def __init__(self, host, port, application):
        asyncore.dispatcher.__init__ (self)
        self.host = host
        self.port = port
        self.application = application
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((self.host, port))
        self.listen(5)
        self.setup_environ()
        
    def setup_environ(self):
        env = self.base_environ = {}
        env['SERVER_NAME'] = self.socket.getsockname()
        env['GATEWAY_INTERFACE'] = 'CGI/1.1'
        env['SERVER_PORT'] = str(self.port)
        env['REMOTE_HOST']=''
        env['CONTENT_LENGTH']=''
        env['SCRIPT_NAME'] = ''

    def handle_accept(self):
        """ For python 2 compatibility """
        pair = self.accept()
        if pair is not None:
            self.handle_accepted(*pair)


    def handle_accepted(self, sock, addr):
        AsynWsgiRequestHandler(sock, addr, self)


    def get_app(self):
        return self.application
        




        
        
html1 = """
<html>
<body>
   <form enctype="multipart/form-data" method="post" action="">
        <p>File:<input type='file' name='file'></p>
        <input type="submit" name="submit" value="upload"/>  
   </form>
   <p>
      Age: %s<br>
      Hobbies: %s
      </p>
</body>
</html>"""
html = """
<html>
<body>
   <form method="get" action="">
      <p>
         Age: <input type="text" name="age">
         </p>
      <p>
         Hobbies:
         <input name="hobbies" type="checkbox" value="software"> Software
         <input name="hobbies" type="checkbox" value="tunning"> Auto Tunning
         </p>
      <p>
         <input type="submit" value="Submit">
         </p>
      </form>
   <p>
      Age: %s<br>
      Hobbies: %s
      </p>
   </body>
</html>"""
def application(environ,start_response):
    d = cgi.parse_qs(environ['QUERY_STRING'])
    print("in application")
    print(environ)
    print(environ['QUERY_STRING'])
    age = d.get('age',[''])[0]
    hobbies = d.get('hobbies',[])
    age = cgi.escape(age)
    hobbies = [cgi.escape(hobby) for hobby in hobbies]
    response_body = html % (age or 'Empty',
                    ','.join(hobbies or ['no hobbies'])
                    )
    status = '200 OK'
    response_headers = [('Content-Type','text/html'),
                ('Content-Length',str(len(response_body)))
                ]
    start_response(status,response_headers)
    #response_body = response_body.encode('ascii')
    return [response_body]

if __name__ == "__main__":
    # Create the web server on port 8000
    port = 8000
    print("Open http://localhost:" + str(port))
    WsgiServer("", port, application)
    try:
        # Start asyncore's event loop
        asyncore.loop()
    except KeyboardInterrupt:
        pass