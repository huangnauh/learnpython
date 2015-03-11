#!/usr/bin/env python
# coding: utf-8
from multiprocessing import Process,Queue,Pipe
import ipdb
def proc1(conn):
    conn.send([42,None,"hello"])
    print "proc1:",conn.recv()

def proc2(conn):
    print "proc2:",conn.recv()
    conn.send("hello")
    conn.send('haha')

if __name__ == "__main__":
    pipe = Pipe()
    p2 = Process(target=proc2,args=(pipe[1],))
    p2.start()
    proc1(pipe[0])
    p2.join()
