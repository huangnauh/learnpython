class Data(object):
    def __init__(self):
        self._data=[]
    
    def add(self,x):
        self._data.append(x)
    
    def data(self):
        return iter(self._data)
#迭代器
class Data(object):
    def __init__(self,*args):
        self._data=list(args)
    def __iter__(self):
        return DataIter(self)
        
class DataIter(object):
    def __init__(self,data):
        self._index=0
        self._data=data._data
    def next(self):
        if self._index >= len(self._data) : raise StopIteration
        d=self._data[self._index]
        self._index +=1
        return d
#迭代器

#生成器
class Data(object):
    def __init__(self,*args):
        self._data=list(args)
    def __iter__(self):
        for x in self._data:
            yield x


#生成器

#coroutine
def framework(logic):
    try:
        it=logic()
        s=next(it)
        print "logic:",s
        print "logic:",s
        it.send("async"+s)
    except StopIteration:
        pass
def logic():
	s='mylogic'
	r = yield s
	print r

#callback回调
def framework(logic,callback):
	s=logic()
	print "logic:",s
	print "do someting..."
	callback("async"+s)
def logic():
	s='mylogic'
	return s
def callback(s):
	print s
#异常 NameError ZeroDivisionError SyntaxError IndexError KeyError IOError AttributeError
try:
    print adict[5]
except KeyError:
