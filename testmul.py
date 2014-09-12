import os
import threading
import multiprocessing
from time import sleep

# worker function
def worker(sign,lock):
    with lock:
		print(sign, os.getpid())
		sleep(2)

if __name__ == "__main__":
	print('Main:',os.getpid())
	record = []
	lock = multiprocessing.RLock()
	for i in range(5):
		process = multiprocessing.Process(target=worker,args=('process',lock))
		record.append(process)
	for process in record:
		process.start()
		

	for process in record:
		process.join()