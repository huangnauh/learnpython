#!/usr/bin/env python
# coding: utf-8

from gevent.server import StreamServer
import gevent
def handler(socket,address):
    data = socket.recv(1024)
    for i in xrange(100):
        socket.send('hello:'+str(i)+data)
        gevent.sleep(0)
    socket.close()

server = StreamServer(('127.0.0.1',5000),handler)
server.serve_forever()
