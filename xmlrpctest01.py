from SimpleXMLRPCServer import SimpleXMLRPCServer,list_public_methods
from xmlrpclib import Binary
import logging
import os
import inspect
import datetime
logging.basicConfig(level=logging.DEBUG)
server = SimpleXMLRPCServer(('localhost',9000),logRequests=True,allow_none=True)
server.register_introspection_functions()
server.register_multicall_functions()
class ExampleService:
    def ping(self):
        return True
    def now(self):
        return datetime.datetime.now()
    def show_type(self,arg):
        return (str(arg),str(type(arg)),arg)
    def raises_exception(self,msg):
        raise RuntimeError(msg)
    def send_back_binary(self,bin):
        data = bin.data
        response = Binary(data)
        return response
server.register_instance(ExampleService())

def list_contents(dir_name):
    logging.debug('list_contents(%s)', dir_name)
    return os.listdir(dir_name)
server.register_function(os.listdir,'dir.list')
server.register_function(os.mkdir,'dir.create')
server.register_function(os.rmdir,'dir.remove')
class ServiceRoot:
    pass
class DirectoryService:
    def _listMethods(self):
        return list_public_methods(self)
    def _methodHelp(self,method):
        f = getattr(self,method)
        return inspect.getdoc(f)
    def mylist(self,dir_name):
        """mylist(dir_name) => [<filenames>]
        
        Returns a list containing the contents of the named directory.
        """
        return os.listdir(dir_name)
root = ServiceRoot()
root.dir = DirectoryService()
#server.register_instance(DirectoryService(),allow_dotted_names=True)

def expose(f):
    f.exposed = True
    return f

def is_exposed(f):
    return getattr(f,'exposed',False)

class MyService(object):
    PREFIX = 'prefix'
    def _dispatch(self,method,params):
        if not method.startswith(self.PREFIX+'.'):
            raise Exception('method "%s" is not supported' % method)
        method_name = method.partition('.')[2]
        func = getattr(self,method_name)
        if not is_exposed(func):
            raise Exception('method "%s" is not supported' % method)
        return func(*params)
    @expose
    def public(self):
        return 'this is public'
    
    def private(self):
        return 'this is private'
#server.register_instance(MyService())


try:
    print("Use Control-C to exit")
    server.serve_forever()
except KeyboardInterrupt:
    print("exiting")