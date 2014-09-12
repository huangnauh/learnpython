from wsgiref.simple_server import make_server,WSGIServer
from SimpleXMLRPCServer import SimpleXMLRPCDispatcher
from SocketServer import ThreadingMixIn
import threading
import time
import os
import cgi
import xmlrpclib
_RESPONSE_STATUSES = {
    # Informational
    100: 'Continue',
    101: 'Switching Protocols',
    102: 'Processing',

    # Successful
    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    203: 'Non-Authoritative Information',
    204: 'No Content',
    205: 'Reset Content',
    206: 'Partial Content',
    207: 'Multi Status',
    226: 'IM Used',

    # Redirection
    300: 'Multiple Choices',
    301: 'Moved Permanently',
    302: 'Found',
    303: 'See Other',
    304: 'Not Modified',
    305: 'Use Proxy',
    307: 'Temporary Redirect',

    # Client Error
    400: 'Bad Request',
    401: 'Unauthorized',
    402: 'Payment Required',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    406: 'Not Acceptable',
    407: 'Proxy Authentication Required',
    408: 'Request Timeout',
    409: 'Conflict',
    410: 'Gone',
    411: 'Length Required',
    412: 'Precondition Failed',
    413: 'Request Entity Too Large',
    414: 'Request URI Too Long',
    415: 'Unsupported Media Type',
    416: 'Requested Range Not Satisfiable',
    417: 'Expectation Failed',
    418: "I'm a teapot",
    422: 'Unprocessable Entity',
    423: 'Locked',
    424: 'Failed Dependency',
    426: 'Upgrade Required',

    # Server Error
    500: 'Internal Server Error',
    501: 'Not Implemented',
    502: 'Bad Gateway',
    503: 'Service Unavailable',
    504: 'Gateway Timeout',
    505: 'HTTP Version Not Supported',
    507: 'Insufficient Storage',
    510: 'Not Extended',
}
class Stats:
    def __init__(self):
        self.lock = threading.RLock()
    def getstats(self):
        return self.callstats
    def getruntime(self):
        return time.time() - self.start
    def failure(self):
        raise RuntimeError('error')
class Math(Stats):
    def __init__(self):
        print("in init")
        self.callstats = {'pow' : 0,'hex':0}
        self.start = time.time()
        Stats.__init__(self)
    def pow(self,x,y):
#        self.lock.acquire()
        self.callstats['pow'] += 1
#        time.sleep(1)
#        self.lock.release()
        print(threading.currentThread())
#        print(os.getpid())
        return pow(x,y)
        
    def hex(self,x):
#        self.lock.acquire()
        self.callstats['hex'] += 1
#        time.sleep(1)
#        self.lock.release()
        return "%x" % x
    
    def sortlist(self,l):
        l = list(l)
        l.sort()
        return l


class ThreadingWSGIServer(ThreadingMixIn,WSGIServer):
    pass
        
 
class WSGIXMLRPCApplication:
    def __init__(self,instance=None,methods=[]):
        self.dispatcher = SimpleXMLRPCDispatcher(allow_none=True,encoding=None)
        if instance is not None:
            self.dispatcher.register_instance(instance)
        for method in methods:
            self.dispatcher.register_function(method)
        self.dispatcher.register_introspection_functions()
    def __call__(self,environ,start_response):
        if environ["REQUEST_METHOD"] == "POST":
            return self.handle_post(environ,start_response)
        else:
            start_response("400 Bad request",[("Content-Type","text/plain")])
            return ['']
    def handle_post(self,environ,start_response):
        try:
            max_chunk_size = 10*1024*1024
            size_remaining = int(environ["CONTENT_LENGTH"])
            L = []
            rfile = environ['wsgi.input']
            while size_remaining:
                chunk_size = min(size_remaining, max_chunk_size)
                chunk = rfile.read(chunk_size)
                if not chunk:
                    break
                L.append(chunk)
                size_remaining -= len(L[-1])
            data = ''.join(L)
            

            data = self.decode_request_content(data,environ,start_response)
            if isinstance(data, list):
                return data 
            response = self.dispatcher._marshaled_dispatch(data)
        except Exception, e: 
            start_response("%d %s" % (500,_RESPONSE_STATUSES[500]),[
            ("Content-length", '')
            ])
            return []
        else:
            start_response("%d %s" % (200,_RESPONSE_STATUSES[200]),[
                ('Content-Type','text/xml'),
                ("Content-length", str(len(response)))
                ])
            return [response]
            
    def decode_request_content(self, data,environ,start_response):
        #support gzip encoding of request
        encoding = environ.get("HTTP_CONTENT_ENCODING", "identity").lower()
        if encoding == "identity":
            return data
        if encoding == "gzip":
            try:
                return xmlrpclib.gzip_decode(data)
            except NotImplementedError:
                response = "encoding %r not supported" % encoding
                start_response("%d %s" % (501,_RESPONSE_STATUSES[501]),[
                ("Content-length", str(len(response)))
                ])
            except ValueError:
                response = "error decoding gzip content"
                start_response("%d %s" % (400,_RESPONSE_STATUSES[400]),[
                ("Content-length", str(len(response)))
                ])
        else:
            response = "encoding %r not supported" % encoding
            start_response("%d %s" % (501,_RESPONSE_STATUSES[501]),[
            ("Content-length", str(len(response)))
            ])  
        return [response]
        
    
server = make_server('localhost',8080,WSGIXMLRPCApplication(Math(),[int]),server_class=WSGIServer)
server.serve_forever()