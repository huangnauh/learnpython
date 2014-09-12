import threading
import Queue
from time import ctime,sleep
import random
class MyThread(threading.Thread):
	def __init__(self,func,args,name):
		threading.Thread.__init__(self)
		self.func = func
		self.args = args
		self.name = name
	def run(self):
		print "start ",self.name," at:",ctime()
		self.res = self.func(*self.args)
		print "end ",self.name," at:",ctime()
	def result(self):
		return self.res
		
def writeQ(queue):
	print "producting object"
	queue.put("abc",1)
	print "size now {0}".format(queue.qsize())
	
def readQ(queue):
	queue.get(1)
	print "consumed object"
	print "size now {0}".format(queue.qsize())
	
def writer(queue,loops):
	for i in range(loops):
		writeQ(queue)
		sleep(random.randint(1,3))

def reader(queue,loops):
	for i in range(loops):
		readQ(queue)
		sleep(random.randint(2,5))
		
funcs = [writer,reader]

def main():
	n = range(len(funcs))
	loops = random.randint(2,5)
	threads = []
	q = Queue.Queue(32)
	for i in n:
		t=MyThread(funcs[i],(q,loops),funcs[i].__name__)
		threads.append(t);
	for i in n:
		threads[i].start()
	for i in n:
		threads[i].join()

if __name__ == "__main__":
	main()