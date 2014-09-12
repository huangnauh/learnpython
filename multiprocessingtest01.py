# coding:utf-8

def run(self):
    def f(x):
        return x*x
    p = Pool()
    return p.map(f, [1,2,3])#直接传入函数f

def test():
    cl = calculate()
    print cl.run()#抛出cPickle.PicklingError异常


import multiprocessing
def unwrap_self_f(arg, **kwarg):
    return calculate.f(*arg, **kwarg)#返回一个对象
class calculate(object):
    def f(self,x):
        return x*x
    def run(self):
        p = multiprocessing.Pool()
        return p.map(unwrap_self_f, zip([self]*3,[1,2,3]))
        
if __name__ == "__main__":
    cl = calculate()
    print cl.run()
    
    