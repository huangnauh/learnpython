#encoding=utf-8
import threading
import random
import time
from Queue import Queue
from collections import deque
MAX_NUM = 3
cond = threading.Condition()
class Producer(threading.Thread):

   def __init__(self, threadname, queue):
       threading.Thread.__init__(self, name = threadname)
       self.sharedata = queue

   def run(self):
       for i in range(10):
           with cond:
               if len(self.sharedata) == MAX_NUM:
                   print "Queue full, producer is waiting"
                   cond.wait()
               self.sharedata.append(i)
               print self.getName(),'adding',i,'to queue'
               cond.notify()
           time.sleep(random.randrange(10)/10.0)
               
       print self.getName(),'Finished'


class Consumer(threading.Thread):

   def __init__(self, threadname, queue):
       threading.Thread.__init__(self, name = threadname)
       self.sharedata = queue

   def run(self):
       for i in range(10):
           with cond:
               if not self.sharedata:
                   print "Nothing in queue, consumer is waiting"
                   cond.wait()
               x = self.sharedata.popleft()
               print self.getName(),'got a value:',x
               cond.notify()
           time.sleep(random.randrange(10)/10.0)
       print self.getName(),'Finished'

# Main thread
def main():
   queue = deque()
   producer = Producer('Producer', queue)
   consumer = Consumer('Consumer', queue)
   print 'Starting threads ...'
   producer.start()
   consumer.start()
   producer.join()
   consumer.join()
   print 'All threads have terminated.'

if __name__ == '__main__':
   main()