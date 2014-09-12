#!/usr/bin/env python
# coding: utf-8

import socket,select
response = b"HTTP/1.0 200 OK\r\n"
response += b"Data:Mon 25 Auguest 2014 14:57:01 GMT\r\n"
response += b"Content-Type:text/plain\r\n"
response += b"Content-Length:13\r\n\r\n"
response += b"hello, world!"

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

sock.bind(("",8080))
sock.listen(1)
sock.setblocking(0)
epoll = select.epoll()
epoll.register(sock.filno(),select.EPOLLIN)
try:
    while True:
        client,address = sock.accept()
        request = b""
        while b"\n\n" not in request and b"\n\r\n" not in request:
            request += client.recv(1024)
        print('-'*40+'\n'+request.decode())
        client.send(response)
        client.close()
finally:
    sock.close()

