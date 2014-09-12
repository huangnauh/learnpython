import sqlite3
import cPickle as pickle
db_file = 'todo.db'
def adapter_func(obj):
    print 'adapter_func(%s)\n' % obj
    return pickle.dumps(obj)
    
def converter_func(data):
    print 'converter_func(%r)\n' % data
    return pickle.loads(data)
    
class MyObj(object):
    def __init__(self,arg):
        self.arg = arg
    def __str__(self):
        return 'MyObj(%r)' % self.arg
    def __cmp__(self,other):
        return cmp(self.arg,other.arg)
sqlite3.register_adapter(MyObj,adapter_func)
sqlite3.register_converter(MyObj.__name__,converter_func)

def collation_func(a,b):
    a_obj = converter_func(a)
    b_obj = converter_func(b)
    print 'collation_func(%s,%s)' % (a_obj,b_obj)
    return cmp(a_obj,b_obj)

def authorizer_func(action_code,table,column,sql_location,ignore):
    print '\nauthorizer_func(%s, %s, %s, %s, %s)' % (
            action_code,table,column,sql_location,ignore)
    print '######',sqlite3.SQLITE_SELECT,sqlite3.SQLITE_READ,sqlite3.SQLITE_IGNORE,sqlite3.SQLITE_DENY
    if action_code == sqlite3.SQLITE_SELECT:
        print 'requesting permission to run a select statement'
        response = sqlite3.SQLITE_OK
    elif action_code == sqlite3.SQLITE_READ:
        print 'requesting permission to access the column %s.%s from %s' % (table,column,sql_location)
        response = sqlite3.SQLITE_OK
        if column == 'details':
            print  '  ignoring details column'
            response = sqlite3.SQLITE_IGNORE
        elif column == 'priority':
            print '  preventing access to priority column'
            response = sqlite3.SQLITE_DENY
    return response
    

with sqlite3.connect(db_file,detect_types=sqlite3.PARSE_DECLTYPES) as conn:
    conn.row_factory = sqlite3.Row
    conn.set_authorizer(authorizer_func)
    print 'Using SQLITE_IGNORE to mask a column value:'
    cursor = conn.cursor()
    cursor.execute("select id, details from task where project = 'huang'")
    for row in cursor.fetchall():
        print row['id'], row['details']
    print '\nUsing SQLITE_DENY to deny access to a column:'
    cursor.execute("select id, priority from task where project = 'huang'")
    for row in cursor.fetchall():
        print row['id'], row['priority']
    

def test():
    conn.create_collation('unpickle',collation_func)
    conn.execute('delete from obj')
    conn.executemany('insert into obj (data) values (?)',
                [(MyObj(x),) for x in xrange(5,0,-1)]
                )
    cursor = conn.cursor()
    cursor.execute('select id,data from obj order by data collate unpickle')
    for obj_id,obj in cursor.fetchall():
        print 'retrieved',obj_id,obj,type(obj)
        