import time
a = 1
def f1():
    exec ""
    start = time.clock()
    sum_ = 0
    for i in xrange(100000):
        sum_ += a
    print "with exec:", time.clock() - start

def f2():
    start = time.clock()
    sum_ = 0
    for i in xrange(100000):
        sum_ += a
    print "without exec:", time.clock() - start

f1()
f2()