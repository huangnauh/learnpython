#!/usr/bin/env python
# coding: utf-8

import asynchat
import logging
import socket
import asyncore

class EchoClient(asynchat.async_chat):
    ac_in_buffer_size = 64
    ac_out_buffer_size = 64
    
    def __init__(self,host,port,message):
        self.meaasge = message
        self.received_data = []
        self.logger = logging.getLogger('EchoClient')
        asynchat.async_chat.__init__(self)
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.logger.debug('connecting to %s', (host, port))
        self.connect((host,port))

    def handle_connect(self):
        self.logger.debug('handle_connect()')
        self.push("ECHO %d\n" % len(self.message))
        self.push_with_producer(EchoProducer(self.message,buffer_size=self.ac_out_buffer_size))
        self.set_terminator(len(self.message))

    def collect_incoming_data(self,data):
        self.logger.debug('collect_incoming_data() -> (%d)\n',len(data))
        self.received_data.append(data)

    def found_terminator(self):
        self.logger.debug('found_terminator()')
        received_message = ''.join(self.received_data)
        if received_message == self.message:
            self.logger.debug('RECEIVED COPY OF MESSAGE')
        else:
            self.logger.debug('ERROR IN TRANSMISSION')
            self.logger.debug('RECEIVED "%d"', len(received_message))

class EchoProducer(asynchat.simple_producer):
    logger = logging.getLogger('EchoProducer')
    def more(self):
        response = asynchat.simple_producer.more(self)
        self.logger.debug('more() -> (%s bytes)\n',len(response))
        return response

message_data = open('a.txt','r').read()
client = EchoClient('127.0.0.1',8080,message= message_data)
asyncore.loop()
