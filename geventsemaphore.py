#!/usr/bin/env python
# coding: utf-8

import gevent
from gevent.pool import Pool
from gevent.coros import BoundedSemaphore

sem = BoundedSemaphore(2)

def workers(n):
    sem.acquire()
    print('Worker %i acquired semaphore' % n)
    gevent.sleep(n)
    sem.release()
    print('Worker %i released semaphore' % n)

pool = Pool()
pool.map(workers,xrange(0,4))
