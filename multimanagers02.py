#!/usr/bin/env python
# coding: utf-8

import multiprocessing
import logging

def worker(d,value):
    d.append(value)

if __name__ == "__main__":
    mgr = multiprocessing.Manager()
#    multiprocessing.log_to_stderr(logging.DEBUG)
    d = mgr.list()
    jobs = [multiprocessing.Process(target=worker,args=(d,i))
             for i in range(10)]
    for i in jobs:
        i.start()

    for i in jobs:
        i.join()

    print "results:",d
