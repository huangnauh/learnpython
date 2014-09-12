#!/usr/bin/env python
# coding: utf-8

import gevent
from gevent.local import local

stash = local()

def f1():
    stash.x = 1
    print(stash.x)
    print object.__getattribute__(stash,'__dict__')
    print dict(object.__getattribute__(stash,'_local__dicts'))
    print(id(stash),stash.__dict__)
    return "f1"

def f2():
    stash.y = 2
    print(stash.y)
    print object.__getattribute__(stash,'__dict__')
    print dict(object.__getattribute__(stash,'_local__dicts'))
    print(id(stash),stash.__dict__)
    return 'f2'

g1 = gevent.spawn(f1)
g2 = gevent.spawn(f2)

gevent.joinall([g1,g2])
print "ok"
print stash.__dict__
print dict(object.__getattribute__(stash,'_local__dicts'))
