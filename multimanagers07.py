#!/usr/bin/env python
# coding: utf-8

import multiprocessing
import time
def producer(ns,event):
    time.sleep(0.1)
    ns.value = "this is the value"
    ns.arr.append(5)
    event.set()

def consumer(ns,event):
    try:
        value = ns.value
    except Exception,err:
        print "Before event,consumer got:",str(err)
    event.wait()
    print 'After event, consumer got:', ns.arr

if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    namespace = mgr.Namespace()
    namespace.arr = [1,2,3,4]
    event = multiprocessing.Event()
    p = multiprocessing.Process(target=producer, args=(namespace, event))
    c = multiprocessing.Process(target=consumer, args=(namespace, event))
    
    c.start()
    p.start()
    
    c.join()
    p.join()

