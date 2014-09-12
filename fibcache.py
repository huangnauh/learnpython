cache = {0:0,1:1}
def fib(n):
	if not n in cache:
		cache[n]=fib(n-1)+fib(n-2)
	return cache[n]