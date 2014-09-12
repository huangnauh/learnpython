#!/usr/bin/env python
# coding: utf-8

import multiprocessing
import logging
class MyFancyClass(object):
    def __init__(self,name):
        self.name = name

    def do_something(self):
        proc_name = multiprocessing.current_process().name
        print proc_name,self.name

def worker(q):
    obj = q.get()
    obj.do_something()

if __name__ == "__main__":
    multiprocessing.log_to_stderr(logging.DEBUG)
    queue = multiprocessing.Queue()

    p = multiprocessing.Process(target=worker,args=(queue,))
    p.start()
    queue.put(MyFancyClass("Fancy hu"))

    queue.close()
    print("join_thread\n")
    queue.join_thread()
    print("process join\n")
    p.join()
