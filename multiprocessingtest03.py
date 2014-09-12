#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process,Value,Array,Lock
import pdb
import multiprocessing
import time
import ipdb
import sys
class ForkedPdb(pdb.Pdb):
    def interaction(self,*args,**kwargs):
        _stdin = sys.stdin
        try:
            sys.stdin = file("/dev/stdin")
            pdb.Pdb.interaction(self,*args,**kwargs)
        finally:
            sys.stdin = _stdin

def proc1(lock,num,arr,pid):
#    pdb.Pdb(stdin=open('p_in', 'r+'), stdout=open('p_out', 'w+')).set_trace()

    with lock:
        #print("pid %s lock %s num %s arr %s" % (pid,id(lock),id(num),id(arr)))
        print(lock,num)
    num.value += 1
    for i in arr:
        i = pid
    with lock:
        #print("pid %s lock %s num %s arr %s" % (pid, id(lock),id(num),id(arr)))
        print(lock,num)
        for i in arr:
            print i,


if __name__ == "__main__":
    lock = Lock() 
    logger = multiprocessing.log_to_stderr()
    logger.setLevel(multiprocessing.SUBDEBUG)
    num = Value('d',0.0)
    arr = Array('i',range(10))
    for i in xrange(1):
        p = Process(target=proc1,args=(lock,num,arr,i))
        p.start()

#    pdb.set_trace()
    for i in xrange(1):
        p.join()
    print(num.value)
    arr[0] = 12
