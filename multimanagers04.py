#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Manager
import multiprocessing
import os
import time 
 
def testFunc(nsum,cc,x):
    for i in xrange(10):
        time.sleep(0.1)
        x.append(i)
        nsum.x = x
 
def test():
    threads = []
    manager = Manager()
#    lock = multiprocessing.Lock() 
#    nsum = manager.list([1,2,3,[1,2,3]])
    nsum = manager.Namespace(x=[])
#    rlock = manager.RLock()
#    nsum = multiprocessing.Value('i',0)
    for i in range(1):
        t = Process(target=testFunc, args=(nsum,1,nsum.x))
        t.daemon = True
        threads.append(t)
    for i in range(len(threads)):
        threads[i].start()
    for j in range(len(threads)):
        threads[j].join()
 
    print "------------------------"
    print 'process id:', os.getpid()
    print nsum.x

if __name__ == '__main__':
    import timeit
    test()
#    print(timeit.timeit("test()",number=10,setup="from __main__ import test"))
