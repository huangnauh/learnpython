import socket
from functools import partial
class LazyConnection:
    def __init__(self,address,
        family=socket.AF_INET,type=socket.SOCK_STREAM):
        self.address = address
        self.type = type
        self.family = family
        self.sock = None
    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket.socket(self.family,self.type)
        self.sock.connect(self.address)
        return self.sock
        
    def __exit__(self,exc_type,exc_value,traceback):
        print(exc_type,exc_value,traceback)
        self.sock.close()
        self.sock = None
        
if __name__ == '__main__':
    conn = LazyConnection(('www.python.org', 80))
    with conn as s:
        s.send(b'GET /3/tutorial/index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv,10),b''))
    print(resp)