#!/usr/bin/env python
# coding: utf-8

import gevent

def foo(x,y):
    print('running in foo',x,y)
    gevent.sleep(1)
    print('explicit context switch to foo again')
    return x+y

def bar(z):
    print("explict context to bar",z)
    gevent.sleep(0)
    print("Implicit context switch back to bar")
    gevent.sleep(0)
    print("yes it is")
    return 2*z

#gevent.joinall([
#    gevent.spawn(foo,10,20),
#    gevent.spawn(bar,100)
#    ])
gevent.spawn(foo,10,20).join()
gevent.spawn(bar,100).join()
