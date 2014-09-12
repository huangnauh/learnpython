import cPickle as pickle
import codecs
class TextReader:
    def __init__(self,filename):
        self.filename = filename
        self.file = open(filename)
        self.postion = self.file.tell()
    def readline(self):
        self.file.seek(self.postion)
        line = self.file.readline()
        self.postion = self.file.tell()
        if not line:
            return None
        if line[:3] == codecs.BOM_UTF8:
            line = line[3:]
        return "%i:%s" % (self.postion,line.decode('utf-8'))
    def __getstate__(self):
        state = self.__dict__.copy()
        del state['file']
        return state
        
    def __setstate__(self,state):
        self.__dict__.update(state)
        file = open(self.filename)
        self.file = file

reader = TextReader('test.txt')
print(reader.readline())
print(reader.readline()) 
s = pickle.dumps(reader)
new_reader = pickle.loads(s)
print(new_reader.readline())