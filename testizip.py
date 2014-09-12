class ZipException(Exception):
	pass
def repeat(object,times=None):
	if times is None:
		while 1:
			yield object
	else:
		for i in xrange(times):
			yield object
			
def chain(*iterables):
	for it in iterables:
		for i in it:
			yield i
		
def izip_longest(*args,**kwargs):
	fillvalue = kwargs.get('fillvalue')
	counter = [len(args)-1]
	def sentinel():
		if not counter[0]:
			raise ZipException
		counter[0] -= 1
		yield fillvalue
	fillers = repeat(fillvalue)
	its = [chain(it, sentinel(), fillers) for it in args]
	try:
		while its:
			yield tuple(map(next,its))
	except ZipException:
		pass

def test():	
	it = izip_longest("abc", [1, 2],[1,2,3,4,5], fillvalue = 0)
	print list(it)

import collections
c = collections.Counter({'red': 4, 'blue': 2}) 