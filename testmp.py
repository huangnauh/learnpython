import multiprocessing
import multiprocessing as mp
import time
import random
import sys

def calc(func,args):
	res = func(*args)
	return '%s says that %s%s = %s' % (
        mp.current_process().name,
        func.__name__, args, res
        )
def calculatestar(args):
    return calc(*args)
	
def mul(a, b):
	time.sleep(0.5 * random.random())
	return a * b

def plus(a, b):
	time.sleep(0.5 * random.random())
	return a + b

def f(x):
	return 1.0 / (x - 5.0)

def pow3(x):
	return x ** 3

def noop(x):
	pass

def test():
	PROCESSES = 4
	print('Creating pool with %d processes\n' % PROCESSES)
	with mp.Pool(PROCESSES) as pool:
		Tasks = [(mul,(i,7)) for i in range(10)] + [
				(plus, (i, 8)) for i in range(10)]
		res = [pool.apply_async(calc,t) for t in Tasks]
		imap_it = pool.imap(calculatestar,Tasks)
		impa_unordered_it = pool.imap_unordered(calculatestar, Tasks)
		print('Ordered results using pool.apply_async():')
		for r in res:
			print('\t',r.get())
		print()
		print('Ordered results using pool.imap():')
		for x in imap_it:
			print('\t',x)
		print()
		print('UnOrdered results using pool.imap_unordered():')
		for x in impa_unordered_it:
			print('\t',x)
		
		print("Ordered results using pool.map() --- will block till complete:")
		for x in pool.map(calculatestar, Tasks):
			print('\t', x)
		print()
		print('Testing error handling:')
		res = pool.apply_async(calc, Tasks[0])
		while 1:
			sys.stdout.flush()
			try:
				sys.stdout.write('hahahahah\n\t%s' % res.get(0.02))
				break
			except mp.TimeoutError:
				sys.stdout.write('.')
		print()
		
		print('Testing IMapIterator.next() with timeout:', end=' ')
		it = pool.imap(calculatestar, Tasks)
		while 1:
			sys.stdout.flush()
			try:
				sys.stdout.write('\n\t%s' % it.next(0.02))
			except StopIteration:
				break
			except mp.TimeoutError:
				sys.stdout.write('.')
		print()
if __name__ == '__main__':
    mp.freeze_support()
    test()