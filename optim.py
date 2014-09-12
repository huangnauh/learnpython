from time import time
abbreviations = ['cf.', 'e.g.', 'ex.', 'etc.', 'fig.', 'i.e.', 'Mr.', 'vs.'] 
t = time() 
for i in range (100000): 
	for w in ('Mr.', 'Hat', 'is', 'chasing', 'the', 'black', 'cat', '.'): 
		if w in abbreviations: 
		#if w[-1] == '.' and w in abbreviations: 
			pass 
print "total run time:"
print time()-t
abbreviations = ['cf.', 'e.g.', 'ex.', 'etc.', 'fig.', 'i.e.', 'Mr.', 'vs.'] 
#abbreviations = ['cf.', 'e.g.', 'ex.', 'etc.', 'fig.', 'i.e.', 'Mr.', 'vs.'] 
t = time() 
abbreviations=dict.fromkeys(abbreviations,True)
for i in range (100000): 
	for w in ('Mr.', 'Hat', 'is', 'chasing', 'the', 'black', 'cat', '.'): 
		#if w in abbreviations: 
		if w[-1] == '.' and w in abbreviations:
			pass 
print "total run time:"
print time()-t


lista=[1,2,3,4,5,6,7,8,9,13,34,53,42,44] 
listb=[2,4,6,9,23]
start=time()
for i in range (100000): 
	for a in range(len(lista)): 
		for b in range(len(listb)): 
			x=lista[a]+listb[b] 
print time()-start
start=time()
na=len(lista)
nb=len(listb)
for i in xrange (100000): 
	for a in range(na): 
		temp=lista[a]
		for b in range(nb): 
			x=temp+listb[b] 
print time()-start




start=time()
for i in range (100000): 
	x=[a for a in lista for b in listb if a==b]
print time()-start
print x
start=time()
for i in range (100000): 
	x=list(set(lista)&set(listb)) 	
print time()-start
print x


list = ['a','b','is','python','jason','hello','hill','with','phone','test', 
'dfdf','apple','pddf','ind','basic','none','baecr','var','bana','dd','wrd'] 
#list = dict.fromkeys(list,True) 
print list
filter = []
start=time()
for i in range (100000): 
	for find in ['is','hat','new','list','old','.']: 
		if find not in list: 
			filter.append(find)
print time()-start
list = dict.fromkeys(list,True) 
start=time()
for i in range (100000): 
	for find in ['is','hat','new','list','old','.']: 
		if find not in list: 
			filter.append(find)
print time()-start
