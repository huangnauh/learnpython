import sys
import timeit
def Stack():
    items = []
    def push(item):
        items.append(item)
    def pop():
        return items.pop()
    return  ClosureInstance()   
    
class ClosureInstance:
    def __init__(self,locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals
        
        self.__dict__.update((key,value) for key,value in locals.items()
                            if callable(value))
    def __len__(self):
        return self.__dict__['__len__']()
        
class Stack2():
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def __len__(self):
        return len(self.items)

if __name__ == '__main__':        
    s = Stack()
    print(timeit.timeit('s.push(1);s.pop()','from __main__ import s'))
    s = Stack2()
    print(timeit.timeit('s.push(1);s.pop()','from __main__ import s'))
        
        