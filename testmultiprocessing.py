import multiprocessing as mp
import multiprocessing.managers as managers
import operator

class Foo():
    def f(self):
        print('you called Foo.f()')
    def g(self):
        print('you called Foo.g()')
    def _h(self):
        print('you called Foo._h()')
		

def baz():
    for i in range(10):
        yield i*i
		
class GeneratorProxy(managers.BaseProxy):
	_exposed_ = ['__next__']
	def __iter__(self):
		return self
	def __next__(self):
		return self._callmethod('__next__')
		
class MyManager(managers.BaseManager):
	pass
	
def get_operator_module():
    return operator
	
MyManager.register('Foo1',Foo)
MyManager.register('Foo2',Foo,exposed=('g','_h'))
MyManager.register('baz',baz,proxytype=GeneratorProxy)
MyManager.register('operator',get_operator_module)

def test():
	m = MyManager()
	m.start()
	print('-'*20)
	f1 = m.Foo1()
	f1.f()
	f1.g()
	assert not hasattr(f1,'_h')
	assert sorted(f1._exposed_) == sorted(['f', 'g'])
	print('-'*20)
	f2 = m.Foo2()
	f2.g()
	f2._h()
	assert not hasattr(f2,'f')
	assert sorted(f2._exposed_) == sorted(['_h', 'g'])
	print('-'*20)
	it = m.baz()
	for i in it:
		print('<%d>' % (i,) ,end=' ')
	
	print()
	print(type(it))
	print('-'*20)
	op = m.operator()
	print('op.add(23, 45) =', op.add(23, 45))
	print('op.pow(2, 94) =', op.pow(2, 94))
	print('op._exposed_ =', op._exposed_)

if __name__ == '__main__':
    mp.freeze_support()
    test()
	
	
	
	