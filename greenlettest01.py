from greenlet import greenlet
def test1(a,b):
    print a,b,11111
    print greenlet.getcurrent()
    c = gr2.switch(a+b)
    print c
    return 34
    
def test2(c):
    print c
    print greenlet.getcurrent()
    gr1.switch(c,c+10)
    print 78
    
gr1 = greenlet(test1)
print("gr1",gr1)
gr2 = greenlet(test2)
print("gr2",gr2)
try:
    print(gr2.run)
    d = gr1.run(10,20)
    print d
except KeyError:
    print 'ok'
    
