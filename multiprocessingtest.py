#!/usr/bin/env python
# coding: utf-8

import multiprocessing

from multiprocessing import Process,current_process

def test(*args,**kwargs):
    p = current_process()
    print p.name,p.pid
    print args
    print kwargs

if __name__ == "__main__":
    p = Process(target=test,args=(1,2),kwargs={'a':'hello'},name="TEST")
    p.start()
    p.join()
