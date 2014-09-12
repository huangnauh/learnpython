import weakref
import gc
import pprint

class Graph(object):
	def __init__(self,name):
		self.name = name
		self.other = None
	def set_next(self,other):
		print('%s.set_next(%s,(%s))' % (self.name,other,type(other)))
		self.other = other
	def all_nodes(self):
		yield self
		n = self.other
		while n and n.name != self.name:
			yield n
			n = n.other
		if n is self:
			yield n
		return
	def __str__(self):
		return '->'.join([n.name for n in self.all_nodes()])
	def __repr__(self):
		return '%s(%s)' % (self.__class__.__name__,self.name)
	def __del__(self):
		print('deleting %s' % self.name)
		self.set_next(None)

		
class WeakGraph(Graph):
	def set_next(self,other):
		if other is not None:
			if self in other.all_nodes():
				other = weakref.proxy(other)
		super(WeakGraph,self).set_next(other)


def collect_and_show_garbage():
	print('collecting...')
	n = gc.collect()
	print('unreachable objects:',n)
	print('garbage:')
	pprint.pprint(gc.garbage)



	
def demo(graph_factory):
	print('set up graph')
	one = graph_factory('one')
	two = graph_factory('two')
	three = graph_factory('three')
	one.set_next(two)
	two.set_next(three)
	three.set_next(one)
	print(one)
	print(two)
	print(three)
	collect_and_show_garbage()
	three = None
	two = None
	print('After 2 references removed:')
	print(one)
	collect_and_show_garbage()
	print('Removing last reference:')
	one = None
	collect_and_show_garbage()

if __name__ == '__main__':
	demo(Graph)
	demo(WeakGraph)