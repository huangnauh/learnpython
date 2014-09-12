#!/usr/bin/env python
# coding: utf-8

from gevent import server
from multiprocessing import cpu_count,Process,current_process

master_listen = ('127.0.0.1',5000)
master = server.StreamServer(master_listen,echo)

number_of_processes = 1
print "starting %s processes" % number_of_processes

def server_forever(server):
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

for i in range(number_of_processes):
    Process(target=serve_forever,args=(master,)).start()

s.server_forever()
