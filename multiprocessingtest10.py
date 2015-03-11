# coding=utf-8
import time
from multiprocessing import Process, Value,Array,Manager,Lock
import multiprocessing
import os
#lock = Lock()
#lock = Lock()
def func(val):
    for i in range(10):
        time.sleep(0.1)
        for i in range(len(val)):
             with val.get_lock():
                val[i] = val[i] + 1
#            val.value += 1
            
            
def f1(ns):
    x = ns.x[:]
    x.append(1)
    ns.x = x
    ns.y.append('a')
    
    
def f(ns,x,y):
    x.append(1)
    y.append('a')
    ns.x= x #将可变对象也作为参数传入
    ns.y = y


def testFunc(nsum,cc,lock):
    for i in xrange(10):
        time.sleep(0.1)
        with lock:
            nsum.value += cc

def test3():
    manager = Manager()
    nsum = manager.Value('tmp', 0)
    threads = []
    lock = manager.RLock()
    for ll in range(10):
        t = Process(target=testFunc, args=(nsum,1,lock))
        t.daemon = True
        threads.append(t)

    for i in range(len(threads)):
        threads[i].start()

    for j in range(len(threads)):
        threads[j].join()

    print "------------------------"
    print 'process id:', os.getpid()
    print nsum.value    
    
def test():
    val = Array('i',[0]*10)                           #使用value来共享内存 
    print val[:]
    processList = [Process(target=func, args=(val,)) for i in range(10)]
    for p in processList: p.start()
    for p in processList: p.join()
    print val[:]
    
def test2():
    manager = multiprocessing.Manager()
    ns = manager.Namespace()
    ns.x = [] #manager内部包括可变对象
    ns.y = [] 
    print 'before process operation:', ns,id(ns.x)
#    p = multiprocessing.Process(target=f1,args=(ns,))
    p = multiprocessing.Process(target=f, args=(ns,ns.x,ns.y))
    p.start()
    p.join()
    print 'after process operation', ns,id(ns.x)       #修改根本不会生效

    
def sharedvalues_func(values, arrays, shared_values, shared_arrays):
    for i in range(len(values)):
        v = values[i][1]
        sv = shared_values[i].value
        assert v == sv

    for i in range(len(values)):
        a = arrays[i][1]
        sa = list(shared_arrays[i][:])
        assert a == sa

    print 'Tests passed'

def test_sharedvalues():
    values = [
        ('i', 10),
        ('h', -2),
        ('d', 1.25)
        ]
    arrays = [
        ('i', range(100)),
        ('d', [0.25 * i for i in range(100)]),
        ('H', range(1000))
        ]

    shared_values = [multiprocessing.Value(id, v) for id, v in values]
    shared_arrays = [multiprocessing.Array(id, a) for id, a in arrays]

    p = multiprocessing.Process(
        target=sharedvalues_func,
        args=(values, arrays, shared_values, shared_arrays)
        )
    p.start()
    p.join()
if __name__ == '__main__':
    test3()

    

