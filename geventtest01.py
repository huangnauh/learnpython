#!/usr/bin/env python
# coding: utf-8

from gevent.hub import Waiter,get_hub
result = Waiter()
timer = get_hub().loop.timer(2)
timer.start(result.switch, 'hello from Waiter')
result.get() 
