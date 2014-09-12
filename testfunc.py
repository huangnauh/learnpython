import multiprocessing as mp
import os
import time
import multiprocessing.sharedctypes as sharedctypes
import ctypes
import multiprocessing.managers as managers

def output_result(result,log=None):
	if log is not None:
		log.debug('Got:%r',result)

def add(x,y):
	return x+y

def info(title):
	print(title)
	print('module name:',__name__)
	if hasattr(os,'getppid'):
		print('parent process:',os.getppid())
	print("process id:",os.getpid())

def f1(name):
	info('f function')
	print('hello',name)

def foo1(conn):
	print("in foo")
	conn.send('hahha')
	time.sleep(2)
	conn.close()

def f(n,a):
	n.value = 3.14
	for i in range(len(a)):
		a[i] = -a[i]
	
def f2(x):
	print("process id:",os.getpid(),x)
	time.sleep(1)
	return x**2

def f3(num,arr,l):
	num.value = 3.14
	arr[0] = 10
	l.append('hello')
	
def writer_proc(q):
	print("in writer")
	time.sleep(2)
	q.put(100)
	
def reader_proc(q):
	print("in reader")
	print(q.get())

def foo3(*args,**kwargs):
	print("process id:",os.getpid())
	print(args)
	time.sleep(2)
	print(kwargs)
	return 123
	
def callback(ret):
	time.sleep(2)
	print("return:",ret)
	
class Point(ctypes.Structure):
	_fields_ = [('x',ctypes.c_double),
				('y',ctypes.c_double)]
				
def modify(n,x,s,a):
	n.value **= 2
	x.value *= 3
	s.value = s.value.upper()
	print(a)
	for i in a:
		i.x *=2
		i.y *=2
				
if __name__ == "__main__":
	class QueueManager(managers.BaseManager):
		pass
	QueueManager.register('get_queue',callable=lambda:queue)
	m = QueueManager(address=('127.0.0.1',40000),authkey=b'abc')
	m.connect()
	print('conn1')
	queue = m.get_queue()
	queue.put('hello')
	
def test12():
	lock = mp.Lock()
	n = sharedctypes.Value('i',7)
	x = sharedctypes.Value(ctypes.c_double,1/3,lock=False)
	s = sharedctypes.Array('c',b'hello world',lock=lock)
	a = sharedctypes.Array(Point,
		[(1.875,-6.25), (-5.75,2.0), (2.375,9.5)],lock=lock)
	p = mp.Process(target=modify,args=(n,x,s,a,))
	p.start()
	p.join()
	print(n.value)
	print(x.value)
	print(s.value)
	print([(i.x, i.y) for i in a])


def test11():
	with mp.Pool(processes=3) as pool:
		print(pool.map(f2,range(10)))
		
		for i in pool.imap_unordered(f2,range(10)):
			print(i)
			
		res = pool.apply_async(f2,[10])
		print(res.get(timeout=2))
		res = pool.apply_async(add,(1,2))
		print(res.get(timeout=1))

def test10():
	pool = mp.Pool(3)
	pool.apply_async(foo3,range(3),dict(a=1,b=2),callback=callback)
	ar = pool.apply_async(foo3,'hello',{'hello':'world'})
#	print(ar.get())
	pool.close()
	print("close")
	pool.join()
	


		
		

def test8():
	q = mp.Queue()
	reader = mp.Process(target=reader_proc,args=(q,))
	reader.start()
	writer = mp.Process(target=writer_proc,args=(q,))
	writer.start()
	reader.join()
	writer.join()

def test7():
	server = mp.Manager()
	num = server.Value('d',10.0)
	arr = server.Array('i',range(10))
	l = server.list()
	proc = mp.Process(target=f3,args=(num,arr,l))
	proc.start()
	proc.join()
	print(num.value)
	print(arr)
	print(l)

def test6():
	pool = mp.Pool(3)
	rel = pool.map(f2,[1,2,3,4,5,6,7,8,9])
	print(rel)

def test5():
	num = mp.Value('d',0.0)
	arr = mp.Array('i',range(10))
	p = mp.Process(target=f,args=(num,arr))
	p.start()
	p.join()
	print(num.value)
	print(arr[:])

def test4():
	parent_conn,child_conn = mp.Pipe()
	p = mp.Process(target=foo,args=(child_conn,))
	p.start()
	print(parent_conn.recv())
	p.join()

def test3():
	ctx = mp.get_context('spawn')
	q = ctx.Queue()
	p = ctx.Process(target=foo,args=(q,))
	p.start()
	print(q.get())
	p.join()

def test2():
	mp.set_start_method('spawn')
	q = mp.Queue()
	p = mp.Process(target=foo,args=(q,))
	p.start()
	print(q.get())
	p.join()

def test1():
	info('main')
	p = multiprocessing.Process(target=f,args=('bob',))
	p.start()
	p.join()


def test():
	import logging
	from multiprocessing import Pool
	from functools import partial
	logging.basicConfig(level=logging.DEBUG)
	log = logging.getLogger('test')
	p = Pool()
	p.apply_async(add,(3,4),callback=partial(output_result, log=log))
	p.close()
	p.join()
	