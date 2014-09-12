import threading
import time
class Singleton(object):
    objs =  {}
    objs_locker = threading.Lock()
    def __new__(cls, *args, **kwargs):
        if cls in cls.objs:
            return cls.objs[cls]
        cls.objs_locker.acquire()
        try:
            if cls in cls.objs:
                return cls.objs[cls]
            cls.objs[cls] = object.__new__(cls)
        finally:
            cls.objs_locker.release()
            
class MyObject(Singleton):
    pass
    
def worker1(lock):
    time.sleep(0.1)
    o1 = Singleton()
#    with lock:
#        print "worker1",hex(id(o1)),Singleton.objs
        
def worker2(lock):

    time.sleep(0.1)
    o1 = MyObject()
    with lock:
        print "worker2",hex(id(o1)),Singleton.objs
threads = []
lock = threading.Lock()
for i in xrange(10):    
    p = threading.Thread(target=worker1,args=(lock,))
    threads.append(p)
for i in xrange(10):    
    p = threading.Thread(target=worker2,args=(lock,))
    threads.append(p)
for i in threads:  
    i.start()

for i in threads:  
    i.join()    
print('ok')
print Singleton.objs
