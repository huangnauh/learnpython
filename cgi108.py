from SocketServer import ThreadingMixIn,ForkingMixIn
from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler,CGIXMLRPCRequestHandler
from DocXMLRPCServer import DocXMLRPCServer, DocXMLRPCRequestHandler
import threading
import time
import os
import cgitb
cgitb.enable()
class Stats:
    def __init__(self):
        self.lock = threading.RLock()
    def getstats(self):
        return self.callstats
    def getruntime(self):
        return time.time() - self.start
    def failure(self):
        raise RuntimeError('error')
class Math(Stats):
    def __init__(self):
#        print("in init")
        self.callstats = {'pow' : 0,'hex':0}
        self.start = time.time()
        Stats.__init__(self)
    def pow(self,x,y):
#        self.lock.acquire()
        self.callstats['pow'] += 1
#        time.sleep(1)
#        self.lock.release()
#        print(threading.currentThread())
#        print(os.getpid())
        return pow(x,y)
        
    def hex(self,x):
#        self.lock.acquire()
        self.callstats['hex'] += 1
#        time.sleep(1)
#        self.lock.release()
        return "%x" % x
    
    def sortlist(self,l):
        l = list(l)
        l.sort()
        return l

handler  =  CGIXMLRPCRequestHandler()
handler.register_instance(Math())
handler.register_introspection_functions()
handler.register_function(int)
handler.register_function(list.sort)
handler.handle_request()
def testserver():

    class ThreadingServer(ThreadingMixIn,DocXMLRPCServer):
        pass

    server = DocXMLRPCServer(('localhost',8888),DocXMLRPCRequestHandler,allow_none=True)
    server.set_server_title("Chapter 18 document")
    server.set_server_name("chapter")
    server.set_server_documentation("""welcome""")
    server.register_instance(Math())
    server.register_introspection_functions()
    server.register_function(int)
    server.register_function(list.sort)

def server_run():
    try:
        print("Use Control-C to exit")
        server.serve_forever()
    except KeyboardInterrupt:
        print("exiting")