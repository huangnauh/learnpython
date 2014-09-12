#!/usr/bin/env python
# coding: utf-8

import gevent
from gevent.event import Event

evt = Event()
def setter():
    print("wait for me")
    gevent.sleep(5)
    print('ok')
    evt.set()

def waiter():
    print("I will wait...")
    evt.wait()
    print("now ok")

def main():
    gevent.joinall([
        gevent.spawn(setter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        ])

if __name__ == "__main__":
    main()

