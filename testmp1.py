import multiprocessing as mp
import time
import random
import sys
import queue

def calculate(func, args):
	result = func(*args)
	return '%s says that %s%s = %s' % \
        (mp.current_process().name, func.__name__, args, result)
		
def worker(input,output):
	for func,args in iter(input.get,'STOP'):
		res = calculate(func,args)
		output.put(res)
	print('done')
			
def mul(a, b):
	time.sleep(0.5 * random.random())
	return a * b

def plus(a, b):
	time.sleep(0.5 * random.random())
	return a + b
	
	
	
def test():
	Processes = 4
	Task1 = [(mul,(i,7)) for i in range(20)]
	Task2 = [(plus,(i,8)) for i in range(10)]
	task_queue = mp.Queue()
	done_queue = mp.Queue()
	for task in Task1:
		task_queue.put(task)
	for i in range(Processes):
		mp.Process(target=worker,args=(task_queue,done_queue)).start()
	
	print('Unordered results:')
	for i in range(len(Task1)):
		print('\t', done_queue.get())
	print('now')
	for task in Task2:
		task_queue.put(task)
	for i in range(len(Task2)):
		print('\t', done_queue.get())
		
	for i in range(Processes):
		task_queue.put('STOP')

def test_func(running,mutex):
	random.seed()
	time.sleep(random.random()*4)
	with mutex:
		print('\n\t\t\t' + str(mp.current_process()) + ' has finished')
		running.value -= 1
		
def test_value():
	Tasks = 10
	running = mp.Value('i',Tasks)
	mutex = mp.Lock()
	for i in range(Tasks):
		p = mp.Process(target=test_func,args=(running,mutex))
		p.start()
	while running.value > 0:
		time.sleep(0.08)
		with mutex:
			sys.stdout.write(str(running.value))
			sys.stdout.flush()
	print('ok')


	
def queue_func(q):
	for i in range(30):
		time.sleep(0.5 * random.random())
		q.put(i*i)
	q.put('STOP')
	
def test_queue():
	q = mp.Queue()
	p = mp.Process(target=queue_func,args=(q,))
	p.start()
	o = None
	while o != 'STOP':
		try:
			o = q.get(timeout=0.3)
			print(o)
			sys.stdout.flush()
		except queue.Empty:
			print('TimeOut')

def condition_func(cond):
	cond.acquire()
	print('\t',str(cond))
	time.sleep(2)
	print('\tchild is notifying')
	cond.notify()
	time.sleep(1)
	print('\t',str(cond))
	cond.release()
			
def test_condition():
	cond = mp.Condition()
	p = mp.Process(target=condition_func,args=(cond,))
	print(cond)
	cond.acquire()
	print(cond)
	cond.acquire()
	print(cond)
	p.start()
	print('main is waiting')
	cond.wait()
	print(cond)
	cond.release()
	print(cond)
	cond.release()
	p.join()
	print(cond)
	
def semaphore_func(sema,mutex,running):
	sema.acquire()
	mutex.acquire()
	running.value +=1
	print(running.value,"task in running")
	mutex.release()
	random.seed()
	time.sleep(random.random()*2)
	mutex.acquire()
	running.value -= 1
	print('%s has finished' % mp.current_process())
	mutex.release()
	sema.release()

def test_semaphore():
	sema = mp.Semaphore(3)
	mutex = mp.RLock()
	running = mp.Value('i',0)
	processes = [
			mp.Process(target=semaphore_func,args=(sema,mutex,running))
			for i in range(10)]
	for p in processes:
		p.start()
	for p in processes:
		p.join()
			
def sharedvalues_func(values,arrays,shared_values,shared_arrays):
		for i in range(len(values)):
			values[i][1] = 100
			shared_values[i].values = 100
		for i in range(len(arrays)):
			arrays[i][1][0] = 100
			shared_arrays[i][0] = 100
		print('child:',values)
		print('child:',arrays)

def test_sharedvalues():
	values = [
        ['i', 10],
        ['h', -2],
        ['d', 1.25]
        ]
	arrays = [
        ['i', [1,2,3]],
        ['i', [3,4,5]],
        ['H', [5,6,7]]
        ]
	shared_values = [mp.Value(i,v) for i,v in values]
	shared_arrays = [mp.Array(i,a) for i,a in arrays]
	p = mp.Process(target=sharedvalues_func,
					args=(values,arrays,shared_values,shared_arrays)
					)
	p.start()
	p.join()
	print(values)
	for i in range(len(values)):
		print(shared_values[i].value)
	print(arrays)
	for i in range(len(arrays)):
		print(list(shared_arrays[i]))
		
if __name__ == '__main__':
    test_sharedvalues()