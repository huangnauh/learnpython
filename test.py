from weakref import WeakKeyDictionary

class Descriptor(object):
    def __init__(self, name, default=None):
        self.default = default
        self.name = '_'+name
 
    def __get__(self, instance, owner):
	print "****",
	if not instance:
		return self
        return getattr(instance,self.name,self.default)
 
    def __set__(self, instance, value):
        if callable(callback) and hasattr(instance,callback.__name__):
                callback(value)
        setattr(instance,self.name,value)
    def add_callback(self, instance, callback):
        if hasattr(instance,callback.__name__):
            raise AttributeError("wrong %s" % callback.__name__)
        setattr(instance,callback.__name__,callback)