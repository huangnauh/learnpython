import multiprocessing
import os
import signal
from time import sleep
def test(*args,**kwargs):
	p=multiprocessing.current_process()
	print p.name,p.pid
	print args
	print kwargs
def main():
	p=multiprocessing.Process(target=test,args=(1,2),kwargs = {"a": "hello"}, name = "TEST")
	p.start()
	p.join()
	
class MyProcess(multiprocessing.Process):
	def __init__(self):
		print "init:",os.getpid()
		super(MyProcess,self).__init__()
	def run(self):
		print "run:",os.getpid()

def test1():
	def handle(signum,frame):
		print "child exit.", os.getpid()
		exit(0)
	print "in test"
	signal.signal(signal.SIGTERM,handle)
	while True: sleep(1)

def proc1(pipe):
	pipe.send('hello')
	print 'proc1 rec:',pipe.recv()

def proc2(pipe):
	pipe.send('hello2')
	print 'proc2 rec:',pipe.recv()

def test2(*args,**kwargs):
	sleep(1)
	print os.getpid()
	sleep(2)
	return 123

def callback(ret):
	sleep(2)
	print "return:",ret

def test3(x):
	print multiprocessing.current_process().pid, x
	sleep(1)
	return x + 100
def main2():
	pipe = multiprocessing.Pipe()
	p1 = multiprocessing.Process(target=proc1,args=(pipe[0],))
	p2 = multiprocessing.Process(target=proc2,args=(pipe[1],))
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	
def main3():
	pool = multiprocessing.Pool()
#	pool.apply(test2)
	pool.apply_async(test2, callback=callback)
#	ar=pool.apply_async(test2)
	print "now"
#	print ar.get(1)
#	print "ok"
#	pool.map(test3,xrange(10), chunksize=3)
	print "ok"

	
if __name__ == '__main__' :
	main3()







def main1():
	print "parent:",os.getpid()
	p=multiprocessing.Process(target=test1)
	p.daemon = True
	p.start()
	sleep(2)
	print "parent exit.", os.getpid()