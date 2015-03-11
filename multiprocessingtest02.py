#!/usr/bin/env python
# coding: utf-8

import os
import logging
import multiprocessing
import time
import pdb
import Queue
def inputQ(queue):
#    pdb.Pdb(stdin=open('p_in','r+'),stdout=open('p_out','w+')).set_trace()
    count = 5
    while count > 0:
        count -= 1
        if count % 2 == 0:
            print "count:",count,"buffer:",len(queue._buffer)
        info = "put:"+str(count)
        try:
            queue.put(info,timeout=1)
        except Queue.Full:
            print("Full")

def outputQ(queue,lock):
    info = queue.get()
    with lock:
        print(str(os.getpid())+ " get:"+ str(info))

if __name__ == "__main__":
    lock = multiprocessing.Lock()
    queue = multiprocessing.Queue()
    logger = multiprocessing.log_to_stderr()
    logger.setLevel(multiprocessing.SUBDEBUG)
    r1 = []
    r2 = []
    print(queue._maxsize)
#    queue.cancel_join_thread()
    for i in xrange(1):
        process = multiprocessing.Process(target=inputQ,args=(queue,))
        process.start()
        r1.append(process)

#    for i in xrange(1):
#        process = multiprocessing.Process(target=outputQ,args=(queue,lock))
#        process.start()
#        r2.append(process)
    outputQ(queue,lock)

    for p in r1:
        p.join()
    print("End buffer:",len(queue._buffer))
