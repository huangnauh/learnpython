def update_meta (self, other):
    self.__name__ = other.__name__
    self.__doc__ = other.__doc__
    self.__dict__.update(other.__dict__)
    return self
    
class UserProperty (property):
    def __new__(cls, fget=None, fset=None, fdel=None, doc=None):
        if fget is not None:
            def __get__(obj, objtype=None, name=fget.__name__):
                fget = getattr(obj, name)
                print "fget name:"+fget.__name__
                return fget()
            fget = update_meta(__get__, fget)
        if fset is not None: 
            def __set__(obj, value, name=fset.__name__):
                fset = getattr(obj, name)
                print "fset name:"+fset.__name__
                print "setting value:" +str(value)
                return fset(value)
            fset = update_meta(__set__, fset)
        if fdel is not None:
            def __delete__(obj, name=fdel.__name__):
                fdel = getattr(obj, name)
                print "warning: you are deleting attribute using fdel.__name__"
                return fdel()
            fdel = update_meta(__delete__, fdel)
            return property(fget, fset, fdel, doc)

class C(object):
    def get(self):
        print 'calling C.getx to get value'
        return self._x
    def set(self, x):
        print 'calling C.setx to set value'
        self._x = x
    def delete(self):
        print 'calling C.delx to delete value'
        del self._x
    x = UserProperty(get,set,delete)
    
c = C()
c.x = 1
print c.x
del c.x



def ro_property(obj, name, value):
    setattr(obj.__class__, name, property(lambda obj: obj.__dict__["__" + name]))
    setattr(obj, "__" + name, value)
    
class ROClass(object):
    def __init__(self, name, available):
        self.__t = name
        ro_property(self, "name", name)
        self.available = available
        
a = ROClass("read only", True)
print a.name

print a.__dict__
print ROClass.__dict__
a.__name ="modify"
print a.name