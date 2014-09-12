#!/usr/bin/env python
# coding: utf-8

import asyncore
import socket
import logging
class EchoServer(asyncore.dispatcher):
    def __init__(self,address):
        self.logger = logging.getLogger('EchoServer')
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.bind(address)
        self.address = self.socket.getsockname()
        self.logger.debug("binding to %s",self.address)
        self.listen(1)
    
    def handle_accept(self):
        client_info = self.accept()
        self.logger.debug("handle_accept()-> %s",client_info[1])
        EchoHandler(sock=client_info[0])
        self.handle_close()

    def handle_close(self):
        self.logger.debug("handle_close")
        self.close()

class EchoHandler(asyncore.dispatcher):
    def __init__(self,sock,chunk_size=256):
        self.chunk_size = chunk_size
        self.logger = logging.getLogger("EchoHandler %s" % str(sock.getsockname()))
        asyncore.dispatcher.__init__(self,sock=sock)
        self.data_to_write = []

    def writable(self):
        response = bool(self.data_to_write)
        self.logger.debug("writable()-> %s",response)
        return response

    def handle_write(self):
        data = self.data_to_write.pop()
        sent = self.send(data[:self.chunk_size])
        if sent < len(data):
            remaining = data[sent:]
            self.data_to_write.append(remaining)
        self.logger.debug('handle_write() -> (%d) ', sent)
#        if not self.writable():
#            self.handle_close()

    def handle_read(self):
        data = self.recv(self.chunk_size)
        self.logger.debug('handle_read() -> (%d)', len(data))
        self.data_to_write.insert(0,data)

    def handle_close(self):
        self.logger.debug('handle_close()')
        self.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(name)s: %(message)s',
                        )
    address = ("",8080)
    server = EchoServer(address)
    asyncore.loop()

