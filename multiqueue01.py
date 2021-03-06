#!/usr/bin/env python
# coding: utf-8

import multiprocessing
import time
import random
class Consumer(multiprocessing.Process):
    def __init__(self,task_queue,result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                print "%s:EXiting" % proc_name
                self.task_queue.task_done()
                break
            print "%s:%s" % (proc_name,next_task)
            answer = next_task()
            self.task_queue.task_done()
            self.result_queue.put(answer)

class Task(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __call__(self):
        time.sleep(random.randint(0,10)/10)
        return '%s * %s = %s' % (self.a,self.b,self.a*self.b)
    def __str__(self):
        return "%s * %s" % (self.a,self.b)

if __name__ == "__main__":
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    num_consumers = multiprocessing.cpu_count() *2
    print "creating %d consumers" % num_consumers
    consumers = [Consumer(tasks,results) for i in xrange(num_consumers)]
    for p in consumers:
        p.start()

    num_jobs = 10
    for i in xrange(num_jobs):
        tasks.put(Task(i,i))

    for i in xrange(num_consumers):
        tasks.put(None)

    tasks.join()

    while num_jobs:
        result = results.get()
        print "result:",result
        num_jobs -=1

    
