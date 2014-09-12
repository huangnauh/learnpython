# -*- coding: utf-8 -*-
class TypeSetter(object):
	def __init__(self,fieldtype):
		print "set attribute type",fieldtype
		self.fieldtype = fieldtype
	def is_valid(self,value):
		return isinstance(value,self.fieldtype)
class TypeCheckMeta(type):
	def __new__(cls,name,bases,dt):
		print '-----------------------------------'
		print "Allocating memory for class", name
		print name
		print bases
		print dt
		return super(TypeCheckMeta, cls).__new__(cls,name,bases,dt)
	def __init__(cls,name,bases,dt):
		cls._fields = {}
		for key,value in dt.items():
			if isinstance(value,TypeSetter):
				print "****",value
				cls._fields[key] = value
print('ok')
class TypeCheck(object):
	__metaclass__ = TypeCheckMeta
	def __setattr__(self,key,value):
		print "set attribute value"
		if key in self._fields:
			if not self._fields[key].is_valid(value):
				raise TypeError('Invalid type for field')
		super(TypeCheck,self).__setattr__(key,value)
print('ok')
class MetaTest(TypeCheck):
	name = TypeSetter(str)
	num = TypeSetter(int)
    
    
    
    
    
class Singleton(type):
    def __init__(cls,name,bases,dic):
        super(Singleton,cls).__init__(name,bases,dic)
        cls._instance = None
    def __call__(cls,*args,**kwargs):
        if cls._instance is None:
            print "creating a new instance"
            cls._instance = super(Singleton,cls).__call__(*args,**kwargs)
        else:
            print "warning:only allowed to create one instance,minstance already exists!"
        return cls._instance

class MySingleton(object):
    __metaclass__ = Singleton
    
    
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)
    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance