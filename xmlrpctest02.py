import xmlrpclib
import os.path
import datetime
import pprint
import cPickle as pickle


def test3():
    class MyObj:
        def __init__(self,a,b):
            self.a = a
            self.b = b
        def __repr__(self):
            return 'MyObj(%r, %r)' % (repr(self.a), repr(self.b))

    o = MyObj(1,"b goes here")  
    print 'o=', o
    p = pickle.dumps(o)
    b = xmlrpclib.Binary(p)
    print b
    r  = proxy.send_back_binary(b)
    o3 = pickle.loads(r.data)
    print 'From pickle:', o3, id(o3)

    o2 = MyObj(2, o)
    print 'o2=', o2
    print proxy.show_type(o2) 

def test1():
    path = os.path.abspath('.')
    data = { 'boolean':True, 
             'integer': 1,
             'floating-point number': 2.5,
             'string': 'some text',
             'datetime': datetime.datetime.now(),
             'array': ['a', 'list'],
             'array': ('a', 'tuple'),
             'structure': {'a':'dictionary'},
             }
    arg = []
    for i in range(3):
        d = {}
        d.update(data)
        d['integer'] = i
        arg.append(d)

    print 'Before:'
    pprint.pprint(arg)

    print
    print 'After:'
    pprint.pprint(proxy.show_type(arg)[-1])

def test():
    for method_name in proxy.system.listMethods():
        print '=' * 60
        print method_name
        print '-' * 60
        print proxy.system.methodHelp(method_name)
        print
    print 'public():', proxy.prefix.public()
    try:
        print 'private():', proxy.prefix.private()
    except Exception, err:
        print 'ERROR:', err
    try:
        print 'public() without prefix:', proxy.public()
    except Exception, err:
        print 'ERROR:', err
    print proxy.dir.mylist(path)
    print 'BEFORE       :', 'EXAMPLE' in proxy.dir.list(path)
    print 'CREATE       :', proxy.dir.create(path+'/EXAMPLE')
    print 'SHOULD EXIST :', 'EXAMPLE' in proxy.dir.list(path)
    print 'REMOVE       :', proxy.dir.remove(path+'/EXAMPLE')
    print 'AFTER        :', 'EXAMPLE' in proxy.dir.list(path)
    
    
proxy = xmlrpclib.ServerProxy('http://localhost:9000',verbose=True,encoding='utf-8')
test3()
test1()
multicall = xmlrpclib.MultiCall(proxy)
multicall.show_type(1)
multicall.show_type('string')
for i,r in enumerate(multicall()):
    print i,r