import SimpleHTTPServer
import BaseHTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler

def test(HandlerClass = CGIHTTPRequestHandler,
         ServerClass = BaseHTTPServer.HTTPServer):
    server = ServerClass(("127.0.0.1",9000),HandlerClass)
    server.serve_forever()
    


if __name__ == '__main__':
    test()