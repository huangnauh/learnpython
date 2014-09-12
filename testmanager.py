import multiprocessing.managers as managers
import queue
import multiprocessing as mp
import os
import array
import multiprocessing.connection as connection
class MyManger(managers.BaseManager):
	pass
	
class MathsClass:
	def add(self,x,y):
		return x+y
	def mul(self,x,y):
		return x*y


class Worker(mp.Process):
	def __init__(self, q):
		self.q = q
		super(Worker, self).__init__()
	def run(self):
		print("getpid:",os.getpid())
		self.q.put('local hello')	
		
if __name__ == "__main__":
	address = ('localhost',6000)
	with connection.Listener(address,authkey=b'123') as listener:
		with listener.accept() as conn:
			print("conn accept from:",listener.last_accepted,',',listener.address)
			conn.send(['huang','libo'])
			conn.send_bytes(b'hello')
			conn.send_bytes(array.array('i',[1,2,3,4]))

def test4():

	q = mp.Queue()
	w = Worker(q)
	w.start()
	w.join()
	print('ok')
	class QueueManager(managers.BaseManager): pass

	QueueManager.register('get_queue', callable=lambda: q)
	m = QueueManager(address=('', 30000), authkey=b'abracadabra')
	s = m.get_server()
	s.serve_forever()
	
def test2():
	queue = queue.Queue()
	class QueueManager(managers.BaseManager):
		pass
	QueueManager.register('get_queue',callable=lambda:queue)
	m = QueueManager(address=('127.0.0.1',40000),authkey=b'abc')
	s = m.get_server()
	s.serve_forever()
	
	
def test1():
	MyManger.register('Maths',MathsClass)
	m = MyManger()
	m.start()
	print(m)
	maths = m.Maths()
	print(maths.add(1,2))
	m.shutdown()
	print(m)

def test():
	m = managers.BaseManager(address=('127.0.0.1',50000),authkey=b'abc')
	m.connect()