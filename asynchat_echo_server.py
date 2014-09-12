#!/usr/bin/env python
# coding: utf-8

import asyncore
import socket
import asynchat
import logging

class EchoServer(asyncore.dispatcher):
    def __init__(self,address):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.bind(address)
        self.address = self.socket.getsockname()
        self.listen(1)

    def handle_accept(self):
        client_info = self.accept()
        EchoHandler(sock=client_info[0])
        self.handle_close()

    def handle_close(self):
        self.close()


class EchoHandler(asynchat.async_chat):
    ac_in_buffer_size = 64
    ac_out_buffer_size = 64

    def __init__(self,sock):
        self.received_data = []
        self.logger = logging.getLogger('EchoHandler')
        asynchat.async_chat.__init__(self,sock)
        self.process_data = self._process_command
        self.set_terminator("\n")

    def collect_incoming_data(self,data):
        self.received_data.append(data)
        self.logger.debug('collect_incoming_data() -> (%d bytes)\n',len(data))

    def found_terminator(self):
        self.logger.debug('found_terminator()')
        self.process_data()

    def _process_command(self):
        command = ''.join(self.received_data)
        self.logger.debug('_process_command() "%s"', command)
        command_verb,command_arg = command.strip().split(" ")
        expected_data_len = int(command_arg)
        self.set_terminator(expected_data_len)
        self.process_data = self._process_message
        self.received_data = []

    def _process_message(self):
        to_echo = ''.join(self.received_data)
        self.logger.debug('_process_message() echoing\n')
        self.push(to_echo)
        self.close_when_done()

        
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    )
    address = ('',8080)
    server = EchoServer(address)
    asyncore.loop()
