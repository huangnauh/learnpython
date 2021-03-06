#!/usr/bin/env python
# coding: utf-8

import asyncore
import socket
import logging

class EchoClient(asyncore.dispatcher):
    def __init__(self,host,port,message,chunk_size=512):
        self.message = message
        self.to_send = message
        self.received_data = []
        self.chunk_size = chunk_size
        self.logger = logging.getLogger('EchoClient')
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.logger.debug('connecting to %s', (host, port))
        self.connect((host,port))

    def handle_connect(self):
        self.logger.debug('handle_connect()')

    def handle_close(self):
        self.logger.debug('handle_close()')
        self.close()
        received_message = ''.join(self.received_data)
        if received_message == self.message:
            self.logger.debug('RECEIVED COPY OF MESSAGE')
        else:
            self.logger.debug('ERROR IN TRANSMISSION')
            self.logger.debug('RECEIVED "%d"', len(received_message))
        
    def writable(self):
        self.logger.debug("writable() -> %s", bool(self.to_send))
        return bool(self.to_send)

    def handle_write(self):
        sent = self.send(self.to_send[:self.chunk_size])
        self.logger.debug('handle_write() -> (%d)', sent)
        self.to_send = self.to_send[sent:]

    def handle_read(self):
        data = self.recv(self.chunk_size)
        self.logger.debug('handle_read() -> (%d)', len(data))
        self.received_data.append(data)

if __name__ == '__main__':
    import socket

    logging.basicConfig(level=logging.DEBUG,
                        format='%(name)s: %(message)s',
                        )
    client = EchoClient("127.0.0.1",8080,message=open('a.txt','r').read())
    asyncore.loop()
