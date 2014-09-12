#!/usr/bin/env python
# coding: utf-8

import gevent
import random
def task(pid):
    gevent.sleep(random.randint(0,2)*0.001)
    print("task %d done" % pid)

def synchronous():
    for i in range(1,10):
        task(i)

def asynchronous():
    threads = [gevent.spawn(task,i) for i in xrange(10)]
    gevent.joinall(threads)

print("synchronous:")
synchronous()

print("asynchronous:")
asynchronous()
print('ok')

