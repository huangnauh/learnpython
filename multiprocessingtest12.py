# coding=utf-8
from multiprocessing import Process, Manager
import os
import multiprocessing
manager = Manager()
#vip_list = []
vip_list = manager.list()
def testFunc(cc,vip_list):
    vip_list.append(cc)
    print 'process id:', os.getpid()
 
if __name__ == '__main__':
    multiprocessing.freeze_support()
    threads = []

    for ll in range(10):
        t = Process(target=testFunc, args=(ll,vip_list))
        t.daemon = True
        threads.append(t)
 
    for i in range(len(threads)):
        threads[i].start()
 
    for j in range(len(threads)):
        threads[j].join()
 
    print "------------------------"
    print 'process id:', os.getpid()
    print vip_list