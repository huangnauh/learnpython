#!/usr/bin/env python
# coding: utf-8

import gevent
from gevent.queue import Queue,Empty

tasks = Queue(maxsize=2)

def worker(n):
    try:
        while 1:
            task = tasks.get(timeout=1)
            print("worker %s got task %s" % (n,task))
            gevent.sleep(0)
    except Empty:
        print('quit ')

def boss():
    for i in xrange(1,10):
        tasks.put(i)
    for i in xrange(10,20):
        tasks.put(i)


gevent.joinall([
    gevent.spawn(boss),
    gevent.spawn(worker,'steve'),
    gevent.spawn(worker,"john"),
    gevent.spawn(worker,"huang"),
    gevent.spawn(worker,'ny')])
