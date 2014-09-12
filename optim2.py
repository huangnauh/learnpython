from time import time 
import profile
import pstats
def profileTest():
	Total =1
	for i in range(100000):
		Total = Total*(i+1)
	return Total
profile.run("profileTest()","testprof")
print "******************"
p=pstats.Stats("testprof")
p.sort_stats("name").print_stats()
t = time() 
list = ['a','b','is','python','jason','hello','hill','with','phone','test', 
'dfdf','apple','pddf','ind','basic','none','baecr','var','bana','dd','wrd'] 
total=[]
for i in range (100000): 
	for w in list: 
		total.append(w) 
print "total run time:"
print time()-t
t = time() 
list = ['a','b','is','python','jason','hello','hill','with','phone','test', 
'dfdf','apple','pddf','ind','basic','none','baecr','var','bana','dd','wrd'] 
total=[] 
for i in range (100000): 
	a = (w for w in list)
print "total run time:"
print time()-t