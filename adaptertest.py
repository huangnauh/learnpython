#-*- coding: utf-8 -*-
class Dog(object):
    def __init__(self,name):
        self.name = name
    def bark(self):
        return "wang wang"

class Cat(object):
    def __init__(self,name):
        self.name = name
    def meow(self):
        return "meow"

class AnimalAdapter(object):
    def __init__(self,animal,make_noise):
        self.animal = animal
        self.make_noise = make_noise
        
    def __getattr__(self,attr):   #属性拦截，用于委派属性
        print "****",attr
        return getattr(self.animal,attr)
        
d = Dog('d')
ad = AnimalAdapter(d,d.bark)
c = Cat('c')
ac = AnimalAdapter(c,c.meow)
for i in (ad,ac):
    print i.name,i.make_noise()
    
    
#抽象工厂模式
class CatNoise(object):
    def __init__(self,animal):
        self.animal = animal
    def make_noise(self):
        return self.animal.meow()
        
class DogNoise(object):
    def __init__(self,animal):
        self.animal = animal
    def make_noise(self):
        return self.animal.bark()
        
noise_adapter_lookup = {'Cat':CatNoise,'Dog':DogNoise}

def noise_adapter(animal):
    try:
        return noise_adapter_lookup[animal.__class__.__name__](animal)
    except KeyError:
        raise AdapterLookupError,"Could not find adapter"

# 这个是观察者基类   
class Subject(object):
    def __init__(self):
        self._observers = []
    def attach(self,observer):
        if observer not in self._observers:
            self._observers.append(observer)
            
    def detach(self,observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
            
    def notify(self,modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)
#观察者类           
class Data(Subject):
    def __init__(self, name=''):
        super(Data, self).__init__()
        self.name = name
        self._data = 0
    
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()

# 这里有2个被观察者，也就是依赖的对象，每次Data有改变，这2个view都会变动
class HexViewer(object):
    def update(self, subject):
        print 'HexViewer: Subject %s has data 0x%x' % (subject.name, subject.data)

class DecimalViewer(object):
    def update(self, subject):
        print 'DecimalViewer: Subject %s has data %d' % (subject.name, subject.data)

def test():
    from message import observable
    @observable
    class Foo(object):
        def __init__(self, name):
            print 'hello, %s' % name
            self._name = name
        @property
        def name(self):
            return self._name
        
        @name.setter
        def name(self,value):
            self._name = value
            self.pub('name',value)
            
           
    class HexViewer(object):
        def __init__(self,observer):
            observer.sub('name',self.update)
        def update(self, value):
            print 'Viewer: name change to %s' % (value)

    foo = Foo('lai')
    view1 = HexViewer(foo)
    foo.name = 'huang'
    
if __name__ == '__main__':
    test()
def test1():
    data1 = Data('Data 1')
    data2 = Data('Data 2')
    view1 = DecimalViewer()
    view2 = HexViewer()
    data1.attach(view1)
    data1.attach(view2)
    data2.attach(view2)
    data2.attach(view1)

    print "Setting Data 1 = 10"
    data1.data = 10
    print "Setting Data 2 = 15"
    data2.data = 15
    print "Setting Data 1 = 3"
    data1.data = 3
    print "Setting Data 2 = 5"
    data2.data = 5
    print "Update data1's view2 Because view1 is be filtered"
    data1.notify(modifier=view1)  
    print "Detach HexViewer from data1 and data2."
    data1.detach(view2)
    data2.detach(view2)
    print "Setting Data 1 = 10"
    data1.data = 10
    print "Setting Data 2 = 15"
    data2.data = 15