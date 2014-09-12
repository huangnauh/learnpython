import multiprocessing.managers as managers
import multiprocessing as mp
import array
import multiprocessing.connection as connection

def foo(w):
	for i in range(10):
		w.send((i,mp.current_process().name))
		print("send:",i,mp.current_process().name)
	w.close()

if __name__ == "__main__":
	readers = []
	for i in range(4):
		r,w = mp.Pipe(duplex=False)
		readers.append(r)
		p = mp.Process(target=foo,args=(w,))
		p.start()
		w.close()
	
	while readers:
		for r in connection.wait(readers):
			print('recv:',r)
			try:
				msg = r.recv()
			except EOFError:
				print(r," is done")
				readers.remove(r)
			else:
				print(msg)
				


def test2():
	address = ('localhost',6000)
	with connection.Client(address,authkey=b'123') as client:
		print(client.recv())
		print(client.recv_bytes())
		arr = array.array('i',[0,0,0,0,0,0])
		print(client.recv_bytes_into(arr))
		print(arr)

def test1():
	class QueueManager(managers.BaseManager):
		pass
	QueueManager.register('get_queue',callable=lambda:queue)
	m = QueueManager(address=('127.0.0.1',30000),authkey=b'abracadabra')
	m.connect()
	print('conn1')
	que = m.get_queue()
	print(que)
	p = que.get()
	print('get:',p)