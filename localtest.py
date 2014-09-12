import time

def f1():
    global i, s
    s = 0
    for i in xrange(100000):
        s += i
    return s

def f2():
    s = 0
    for i in xrange(100000):
        s += i
    return s

start = time.clock()
f1()
print "global:", time.clock() - start

start = time.clock()
f2()
print "local:", time.clock() - start