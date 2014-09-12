# coding=utf-8
import Queue
import threading
import random
writelock = threading.Lock()
class Producer(threading.Thread):
    def __init__(self, q,con,name):
        super(Producer, self).__init__()                 
        self.q = q
        self.name = name
        self.con = con
        print "Producer "+self.name+" Started"
    def run(self):
        count=10
        while count:                          
            global writelock                          
            self.con.acquire()                        
            if self.q.full(): 
                with writelock:
                    print 'Queue is full,producer wait!' 
                self.con.wait()
            else: 
                count -= 1
                value = count
                #value = random.randint(0,10) 
                with writelock:
                    print "put value "+self.name+":"+ str(value)+" into queue"
                self.q.put((self.name+":"+str(value)))
                self.con.notify() #通知消费者
                self.con.release() #释放锁对象
class Consumer(threading.Thread):#消费者
    def __init__(self, q,con,name):
        super(Consumer, self).__init__()
        self.q = q
        self.con = con
        self.name = name
        print "Consumer "+self.name+" started\n "
    def run(self):
        count = 20
        while count: 
            global writelock
            self.con.acquire()
            if self.q.empty():#队列为空
                with writelock:
                    print 'queue is empty,consumer wait!'
                self.con.wait()#等待资源 
            else:
                count -= 1
                value = self.q.get()#获取一个元素
                with writelock:
                    print self.name +" get value "+value + " from queue " + str(count)
                self.con.notify()                   #发送消息通知生产者
                self.con.release()                           #释放锁对象
if __name__ == "__main__":
    q = Queue.Queue(10)
    con = threading.Condition()
    p = Producer(q,con,"P1")
    p.start()
    p1 = Producer(q,con,"P2")
    p1.start()
    c1 = Consumer(q,con,"C1")
    c1.start()    