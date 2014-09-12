import eventlet
from eventlet.green import urllib2
from eventlet import event
import time
from Queue import Queue
from threading import Thread
import logging
class Worker(Thread):
    """Thread executing tasks from a given tasks queue"""
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()
    
    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try: 
                body = func(*args, **kargs)
                print("got body", len(body))
            except Exception, e: print e
            self.tasks.task_done()

class ThreadPool:
    """Pool of threads consuming tasks from a queue"""
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads): Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        """Add a task to the queue"""
        self.tasks.put((func, args, kargs))

    def wait_completion(self):
        """Wait for completion of all the tasks in the queue"""
        self.tasks.join()
urls = ["http://www.google.com/intl/en_ALL/images/logo.gif",
       "http://img3.douban.com/icon/ul1078604-88.jpg",
       "http://us.i1.yimg.com/us.yimg.com/i/ww/beta/y3.gif"]

def fetch(url):
     return(urllib2.urlopen(url).read())

def testpoll():
    pool = eventlet.GreenPool()

#    for i in urls:
#        pool.spawn_n(fetch,i)
        
#    pool.waitall()
    for body in pool.imap(fetch, urls):
        print("got body", len(body))

def testthreadpoll():
    pool = ThreadPool(10)
    for i in urls:
        pool.add_task(fetch,i)
    pool.wait_completion()    
        
def test():

    start = time.time()
    testpoll()
    print time.time()-start
    
    start = time.time()
    testthreadpoll()
    print time.time()-start
    
test()