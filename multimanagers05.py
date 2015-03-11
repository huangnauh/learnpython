#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Manager
import multiprocessing
import os
import time 
 
def testFunc(nsum,cc,lock,rlock):
    x = nsum
    start = time.time()
    for i in xrange(100):
        with lock:
            nsum.value += cc
    print 'lock',time.time()-start
    nsum = x
    start = time.time()
    for i in xrange(100):
        with rlock:
            nsum.value += cc
    print 'rlock',time.time()-start
def test():
    threads = []
    manager = Manager()
    lock = multiprocessing.Lock() 
    nsum = manager.Value('tmp', 0)
    rlock = manager.RLock()
#    nsum = multiprocessing.Value('i',0)
    for i in range(1):
        t = Process(target=testFunc, args=(nsum,1,lock,rlock))
        t.daemon = True
        threads.append(t)
    for i in range(len(threads)):
        threads[i].start()
    for j in range(len(threads)):
        threads[j].join()
 
    print "------------------------"
    print 'process id:', os.getpid()
    print nsum.value

if __name__ == '__main__':
    import timeit
    test()
#    print(timeit.timeit("test()",number=10,setup="from __main__ import test"))
