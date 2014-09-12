import time
from collections import deque

num = 100000

def append1(c):
	for i in range(num):
		c.append(i)
	
def appendleft1(c):
	if isinstance(c,deque):
		for i in range(num):
			c.appendleft(i)
	else:
		for i in range(num):
			c.insert(0,i)

def pop1(c):
	for i in range(num):
		c.pop()
		
def popleft1(c):
	if isinstance(c,deque):
		for i in range(num):
			c.popleft()
	else:
		for i in range(num):
			c.pop(0)

def main():
	for container in [deque,list]:
		for operation in [append1,appendleft1,pop1,popleft1]:
			c = container(range(num))
			start = time.time()
			operation(c)
			end = time.time()
			print "Completed {0}/{1} in {2} seconds: {3} ops/sec".format(
              container.__name__, operation.__name__, end-start, num /(end-start))
			
main()