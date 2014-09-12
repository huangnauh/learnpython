__author__ = 'Administrator'

import time
def cleanup():
    time.sleep(10)
    print "in foo hahha"


def upper_attr(future_class_name, future_class_parents,future_class_attr):
    print future_class_name, future_class_parents,future_class_attr
    uppercase_attr = {}
    for name, val in future_class_attr.items():
        if not name.startswith("__"):
            uppercase_attr[name.upper()] = val
        else:
            uppercase_attr[name] = val
    return type(future_class_name, future_class_parents, uppercase_attr)

class UpperAttrMetaClass(type):
    def __new__(cls,clsname,bases,attrs):
        print cls,clsname,bases,attrs
        uppercase_attr = {}
        for name,val in  attrs.items():
            if not name.startswith("__"):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val
        return super(UpperAttrMetaClass,cls).__new__(cls,clsname, bases, uppercase_attr)

    def __init__(self,clsname,bases,attrs):
        print self,clsname,bases,attrs
        super(UpperAttrMetaClass,self).__init__(clsname,bases,attrs)

class FOO1(object):
    def __new__(cls, *args, **kwargs):
        print cls == FOO1
        return super(FOO1,cls).__new__(cls)
    def __init__(self,name,age):
        super(FOO1,self).__init__()

__metaclass__ = UpperAttrMetaClass

myfoo = FOO1('huang',24)

class Foo():
    bar = 'bip'

print(hasattr(Foo,'bar'))
print(hasattr(Foo,'BAR'))