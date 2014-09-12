import Queue
import multiprocessing
from time import sleep

def test(q):
	pid = multiprocessing.current_process().pid
	while True:
		try:
			d = q.get(timeout=2)
			sleep(1)
			print pid,d
			q.task_done()
		except Queue.Empty:
			print pid,"Empty"
			break

if __name__ == "__main__":
	q = multiprocessing.JoinableQueue(maxsize = 1000)
	map(q.put,range(5))
	print "put over"
	for i in range(3):
		multiprocessing.Process(target=test,args=(q,)).start()
	q.join()
	print "task done"