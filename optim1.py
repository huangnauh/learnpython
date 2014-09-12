from time import time
lista=[1,2,3,4,5,6,7,8,9,13,34,53,42,44] 
listb=[2,4,6,9,23]
start=time()
for i in range (100000): 
	x=[a for a in lista for b in listb if a==b]
print time()-start
print x
start=time()
for i in range (100000):
	x=[]
	for a in lista:
		for b in listb:
			if a==b:
				x.append(a)
print time()-start
print x


def func(astr):
	return astr*2
s = ""
list = ['a','b','b','d','e','f','g','h','i','j','k','l','m','n'] 
t = time() 
for i in range (10000): 
	s = ""
	for substr in list: 
		s+= func(substr)
print "total run time:"
print time()-t
print s
s = ""
t = time() 
for i in range (10000): 
	slist = [func(substr) for substr in list]
	x=s.join(slist)
print "total run time:"
print time()-t
print x
print list