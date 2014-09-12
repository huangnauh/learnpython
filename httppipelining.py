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
epoll.register(sock.fileno(),select.EPOLLIN)
try:
    connections = {}
    requests = {}
    responses = {}
    while True:
        events = epoll.poll(1)
        for fileno,event in events:
            print(fileno,event,select.EPOLLIN,select.EPOLLOUT)
            if fileno == sock.fileno():
                client,address = sock.accept()
                client.setblocking(0)
                epoll.register(client.fileno(),select.EPOLLIN)
                connections[client.fileno()] = client
                requests[client.fileno()] = b""
                responses[client.fileno()] = response
            elif event & select.EPOLLIN:
                requests[fileno] += connections[fileno].recv(1024)
                if b"\n\n" in requests[fileno] or b"\n\r\n" in requests[fileno]:
                    epoll.modify(fileno,select.EPOLLOUT)
                    connections[fileno].setsockopt(socket.IPPROTO_TCP,socket.TCP_CORK,1)
                    print('-'*40+'\n'+requests[fileno].decode()[:-2])
            elif event & select.EPOLLOUT:
                byteswritten = connections[fileno].send(responses[fileno])
                responses[fileno] = responses[fileno][byteswritten:]
                if len(responses[fileno]) == 0:
                    connections[fileno].setsockopt(socket.IPPROTO_TCP,socket.TCP_CORK,0)
                    epoll.modify(fileno,0)
                    connections[fileno].shutdown(socket.SHUT_RDWR)
            elif event & select.EPOLLHUP:
                epoll.unregister(fileno)
                connections[fileno].close()
                del connections[fileno]
finally:
    epoll.unregister(sock.fileno())
    epoll.close()
    sock.close()

