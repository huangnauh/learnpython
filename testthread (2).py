#codeing = utf-8
import threading
import time
import urllib2
import Queue
from BeautifulSoup import BeautifulSoup


class MyThread(threading.Thread):

    def __init__(self, func, args, name):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args
        self.name = name

    def run(self):
#        print "start run %s at %s" % (self.name, time.ctime())
        self.res = self.func(*self.args)
#        print "end run %s at %s" % (self.name, time.ctime())

    def getresult(self):
        return self.res


class ThreadHttpUrl(threading.Thread):
    def __init__(self, queue, out_queue):
        super(ThreadHttpUrl, self).__init__()
        self.queue = queue
        self.out_queue = out_queue

    def run(self):
        while True:
            start = time.time()
            try:
                host = self.queue.get(timeout=100)
            except Queue.Empty:
                end = time.time()
                print "****Queue Empty at %s" % (end - start)
                break
            url = urllib2.urlopen(host)
            chunk = url.read()
            self.out_queue.put(chunk)
            self.queue.task_done()
            end = time.time()
            print "%s %s" % (host, end - start)


class ThreadHttpTitle(threading.Thread):
    def __init__(self, out_queue):
        super(ThreadHttpTitle, self).__init__()
        self.out_queue = out_queue

    def run(self):
        while True:
            start = time.time()
            try:
                chunk = self.out_queue.get(timeout=100)
            except Queue.Empty:
                end = time.time()
                print "$$$$$ out_queue Empty at %s" % (end - start)
                break
            soup = BeautifulSoup(chunk)
            print soup.findAll(['title'])
            self.out_queue.task_done()
            end = time.time()
            print "%s" % (end - start)


class WorkMessage(object):
    def _init__(self, thread_num, thread_class):
        self.threads = []
        self.queue = Queue.Queue()
        self.out_queue = Queue.Queue()
        for i in thread_num:
            self.threads.append(thread_class())


def testThreadUrl():
    hosts = ["http://yahoo.com", "http://google.com", "http://amazon.cn", "http://ibm.com",
             "http://baidu.com", "http://yahoo.com", "http://google.com", "http://amazon.cn", "http://ibm.com",
             "http://baidu.com", "http://yahoo.com", "http://google.com", "http://amazon.cn", "http://ibm.com",
             "http://baidu.com"]
    start = time.time()
    threads = []
    nhosts = len(hosts)
    nThreads = nhosts * 2
    queue = Queue.Queue()
    out_queue = Queue.Queue()
    for i in range(nhosts):
        t = ThreadHttpUrl(queue, out_queue)
     #   t.setDaemon(False)
        threads.append(t)
        t = ThreadHttpTitle(out_queue)
        threads.append(t)
    for i in range(nThreads):
            threads[i].start()
    for host in hosts:
        queue.put(host)
    queue.join()
    out_queue.join()
    end = time.time()
    print "elapsed time %s" % (end - start)


def testHttp():
    hosts = ["http://google.com", "http://amazon.cn", "http://ibm.com",
             "http://baidu.com", "http://google.com", "http://amazon.cn", "http://ibm.com",
             "http://baidu.com", "http://google.com", "http://amazon.cn", "http://ibm.com",
             "http://baidu.com"]
    start = time.time()
    for host in hosts:
        url = urllib2.urlopen(host)
        chunk = url.read()
        soup = BeautifulSoup(chunk)
        print soup.findAll(['title'])
    end = time.time()
    print "elapsed time %s" % (end - start)


def geturl(host):
    start = time.time()
    url = urllib2.urlopen(host)
    url.read()
    end = time.time()
    print "%s %s" % (host, end - start)


def testHttpThread():
    hosts = ["http://google.com", "http://amazon.com", "http://ibm.com", "http://baidu.com"]
    threads = []
    start = time.time()
    nhosts = range(len(hosts))
    for host in hosts:
        t = MyThread(geturl, (host,), geturl.__name__)
        threads.append(t)
    for i in nhosts:
        threads[i].start()
    for i in nhosts:
        threads[i].join()
    end = time.time()
    print "elapsed time %s" % (end - start)


def main():
    #testHttp()
    #testThreadUrl()
    print "done"

if __name__ == "__main__":
    main()