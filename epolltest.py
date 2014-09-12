#!/usr/bin/env python
# coding: utf-8

import socket,select
EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
response  = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response += b'Hello, world!'

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind(("",8080))
sock.listen(1)
sock.setblocking(0)

epoll = select.epoll()
epoll.register(sock.fileno(),select.EPOLLIN | select.EPOLLET)

try:
    connections = {}
    requests = {}
    responses = {}
    while True:
        events = epoll.poll(1)
        for fileno,event in events:
            print(fileno,event,select.EPOLLIN,select.EPOLLOUT,select.EPOLLET)
            if fileno == sock.fileno():
                try:
                    while True:
                        client,address = sock.accept()
                        client.setblocking(0)
                        client_fileno = client.fileno()
                        epoll.register(client_fileno,select.EPOLLIN | select.EPOLLET)
                        connections[client_fileno] = client
                        requests[client_fileno] = b""
                        responses[client_fileno] = response
                except socket.error:
                    print("connect",socket.error)
                    pass
            elif event & select.EPOLLIN:
                try:
                    while True:
                        requests[fileno] += connections[fileno].recv(1024)
                except socket.error:
                    print("read",socket.error)
                    pass
                if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                    epoll.modify(fileno,select.EPOLLOUT | select.EPOLLET)
                    print('-'*40 + '\n' + requests[fileno].decode()[:-2])
            elif event & select.EPOLLOUT:
                try:
                    while len(responses[fileno]) > 0:
                        byteswritten = connections[fileno].send(responses[fileno])
                        responses[fileno] = responses[fileno][byteswritten:]
                except socket.error:
                    print('write',socket.error)
                    pass
                if len(responses[fileno]) == 0:
                    epoll.modify(fileno,select.EPOLLET)
                    connections[fileno].shutdown(socket.SHUT_RDWR)
            elif event & select.EPOLLHUP:
                epoll.unregister(fileno)
                connections[fileno].close()
                del connections[fileno]
finally:
    epoll.unregister(sock.fileno())
    epoll.close()
    sock.close()

                

