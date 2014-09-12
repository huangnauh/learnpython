# -*- coding:utf-8 -*-
#cmd /k E: & cd "$(CURRENT_DIRECTORY)" & python "$(FULL_CURRENT_PATH)" & ECHO. & PAUSE & EXIT
import sys,inspect
__builtins__.end = None
def test(x):
	if x>0:
		print "a"
	else:
		print "b"
	end
end
def test1(x):
	for i,j in enumerate(x):
		print "{0}={1}".format(i,j)
end
def test2(x,y=None):
	if y is None :
		y=[]
	y.append(x)
	return y
def test4(a,b,*args,**kwargs):
	print "a,b",a,b
	print "args",args
	print "kwargs",kwargs
def test5(a,b):
	print "a,b",a,b
def test6(a,b,*args,**kwargs):
	c="huang"
	print locals()
def f1():
	x=1
	exec ""
	locals()["x"] = 10
	print x
def foo(): pass
class Child(object):
	def _init__(self,name='huang'):
		self.name=name
	def sayHi(self):
		print self.name,'say Hi!'
def test7(x,y):
	f=inspect.currentframe()
	print f.f_locals
	print f.f_back.f_locals
	try:
		return f
	except:
		print sys.exc_info()
		tb = sys.exc_info()[2]
		print tb
		print tb.tb_lineno
		print tb.tb_frame.f_locals

def main():
#	for i,c in enumerate('abc'):
#		print "s[{0}]={1}".format(i,c)
#	adict={"z":123,"x":456}
#	test6(1,'a','b',**adict)
	a='abc'
	test7(2,0)
end

if __name__ == "__main__":
    main()