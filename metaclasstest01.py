# Base class. Uses a descriptor to set a value
class Descriptor(object):
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)
    def __set__(self, instance, value):
        print "Descriptor in set",instance, value
        instance.__dict__[self.name+'_'] = value
# Descriptor for enforcing types
class Typed(Descriptor):
    expected_type = type(None)
    def __set__(self, instance, value):
        print "Typed in set",instance, value
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        super(Typed,self).__set__(instance, value)
# Descriptor for enforcing values
class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super(Typed,self).__set__(instance, value)

class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super(Typed,self).__init__(name, **opts)
    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super(Typed,self).__set__(instance, value)
        
class Integer(Typed):
    expected_type = int
class UnsignedInteger(Integer, Unsigned):
    pass
class Float(Typed):
    expected_type = float
class UnsignedFloat(Float, Unsigned):
    pass
class String(Typed):
    expected_type = str
class SizedString(String, MaxSized):
    pass
    
    
    
class checkedmeta(type):
    def __new__(cls, clsname, bases, methods):
        # Attach attribute names to the descriptors
        for key, value in methods.items():
            if isinstance(value, Descriptor):
                value.name = key
        return type.__new__(cls, clsname, bases, methods)


# Example
class Stock(object):
    __metaclass__ = checkedmeta
    name   = String()
    shares = Integer()
    def __getattribute__(self,attr):
        print "__getattribute__",attr
        return super(Stock,self).__getattribute__(attr)
    def __setattr__(self,attr,value):
        print "__setattr__",attr,value
        super(Stock,self).__setattr__(attr,value)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price 

s = Stock('huang', 50, 91.1)
print s.__dict__
print s.name