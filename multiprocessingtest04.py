#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Queue
import pdb
def f(q):
    pdb.Pdb(stdin=open("p_in",'r+'),stdout=open('p_out','w+')).set_trace()
    print q.get()    # prints "[42, None, 'hello']"

if __name__ == '__main__':
    q = Queue(3)
    p = Process(target=f, args=(q,))
    p.start()
    pdb.set_trace()
    q.put([42, None, 'hello'])
    p.join()
