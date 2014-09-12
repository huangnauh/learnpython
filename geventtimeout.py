#!/usr/bin/env python
# coding: utf-8

import gevent
from gevent import Timeout

seconds = 3

def wait():
    gevent.sleep(4)

with Timeout(seconds):
    gevent.spawn(wait).join()

