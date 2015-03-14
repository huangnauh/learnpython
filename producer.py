# coding=utf-8
import threading
import Queue
import time
import random
queue = Queue.Queue()
lock = threading.RLock()
class Producer(threading.Thread):
    def __init__(self,queue,valuelist):
        self.queue = queue
        self.values = valuelist
        threading.Thread.__init__(self)
    def run(self):
        for value in self.values:
            self.queue.put(value)
            with lock:
                print "Produced:",value
            time.sleep(random.random())
            
class Consumer(threading.Thread):
    def __init__(self,queue):
        self.queue = queue
        threading.Thread.__init__(self)
    def run(self):
        while True:
            try:
                value = self.queue.get(timeout=2)
                with lock:
                    print threading.currentThread().getName(),"Consumed:",value
                queue.task_done()
            except Queue.Empty:
                with lock:
                    print threading.currentThread().getName(),"Empty"
                break

if __name__ == "__main__" :
    cthread = []
    p = Producer(queue,xrange(8))
    p.start()
    for i in range(3):
        c = Consumer(queue)
        cthread.append(c)
        c.start()  
    p.join()
    for c in cthread:
        c.join()
    