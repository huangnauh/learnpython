#!/usr/bin/env python
# coding: utf-8

import gevent
from gevent.hub import get_hub
from greenlet import greenlet
def test():
    print "OK"
    t = g1.switch()
    print t

def foo():
    while 1:
        print('Running in foo')
        gevent.sleep(0)
        print('Explicit context switch to foo again')

g1 = gevent.spawn(foo)
hub = get_hub()
hub.loop.run_callback(test)

gevent.sleep(0)

