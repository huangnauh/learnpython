#coding=utf-8
import time
import sqlite3
class Cache(object):
    def __init__(self,db,max=10):
        self.mem = {}
        self.time = {}    
        self.max = max
        self.db = db
    def __setitem__(self,key,data,age=None):
        self.mem[key] = data
        if age is None:
            self.time[key] = None
        else:
            self.time[key] = time.time()+age
        if len(self) == self.max:
            self.db.commit(self)
            
    def __getitem__(self,key):
        if key in self.mem:
            if self.time[key] is None or self.time[key] > time.time():
                return self.mem[key]
            else:
                del self[key]
                return None
        else:
            return None 
    def __iter__(self):
        for key in self.mem:
            if self.time[key] is None or self.time[key] > time.time():
                yield key
            else:
                del self[key]
    def __delitem__(self,key):
        del self.mem[key]
        del self.time[key]
    def __len__(self):
        count = 0
        for key in self.mem:
            if self.time[key] is None or self.time[key] > time.time():
                count += 1
            else:
                del self[key]
        return count   
    def clear(self):
        self.mem.clear()
        self.time.clear()
        
class TestDB(object):
    def __init__(self):
        self.conn = sqlite3.connect('test.db')
        cursor = self.conn.cursor()
        cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
        cursor.close()
    def commit(self,cache):
        cursor = self.conn.cursor()
        for i in cache:
            cursor.execute('insert into user (id,name) values (?,?)',(str(i),cache[i]))
        cache.clear()
    def show(self):
        cursor = self.conn.cursor()
        cursor.execute('select * from user')
        values = cursor.fetchall()
        print "db:",values
        cursor.close()
    def close(self):
        self.conn.close()
        
if __name__ == "__main__":
    db = TestDB()
    cache = Cache(db)
    #缓存
    for i in xrange(15):
        cache[i] = "name"+str(i)
    db.show()
    print "cache:",
    for i in cache:
        print [i,cache[i]],
    db.close()
    
    
            