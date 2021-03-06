#!/usr/bin/env python
# coding: utf-8

import gevent
from multiprocessing import Process, Pipe
from gevent.socket import wait_read, wait_write

a,b = Pipe()
c,d = b,a

def relay():
    for i in xrange(10):
        msg = b.recv()
        c.send(msg + ' in '+str(i))

def put_msg():
    for i in xrange(10):
        print 'wait put msg',i
        wait_write(a.fileno())
        a.send('hi')

def get_msg():
    for i in xrange(10):
        print "wait get msg",i
        wait_read(d.fileno())
        print d.recv()


if __name__ == "__main__":
    proc = Process(target=relay)
    proc.start()
    g1=gevent.spawn(get_msg)
    g2=gevent.spawn(put_msg)
    gevent.joinall([g1,g2],timeout=1)

