def test():
    x=[1,2]
    print hex(id(x))
    def a():
        x.append(3)
        print hex(id(x))
    def b():
        print hex(id(x)),x
    return a,b

a,b = test()
a()
b()
print a.func_closure
print b.func_closure

def foo():
    aa=1
    def bar():
        aa=aa+1
    bar()
    print aa