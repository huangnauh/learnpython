#!/usr/bin/env python
# coding: utf-8

import gevent
from gevent.pool import Pool

pool = Pool(2)

def hello_from(n):
    print("size of pool %s" % len(pool))
    print(gevent.getcurrent())

pool.map(hello_from,xrange(3))
