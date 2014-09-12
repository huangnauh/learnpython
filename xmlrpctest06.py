from SocketServer import ThreadingMixIn,ForkingMixIn
from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
from DocXMLRPCServer import DocXMLRPCServer, DocXMLRPCRequestHandler
import threading
import time
import os
class Stats:
    def __init__(self):
        self.lock = threading.RLock()
    def getstats(self):
#        self.lock.acquire()
        callstats=self.callstats
#        self.lock.release()
        return callstats
    def getruntime(self):
        return time.time() - self.start
    def failure(self):
        raise RuntimeError('error')
class Math(Stats):
    def __init__(self):
        print("in init")
        self.callstats = {'pow' : [0],'hex':0}
        self.start = time.time()
        Stats.__init__(self)
    def pow(self,x,y):
#        self.lock.acquire()
        self.callstats['pow'].append(self.callstats['pow'][-1]+1)
#        time.sleep(1)
#        self.lock.release()
        print(threading.currentThread())
#        print(os.getpid())
        return self.callstats['pow']
        
    def hex(self,x):
#        self.lock.acquire()
        self.callstats['hex'] += 1
#        time.sleep(1)
 #       self.lock.release()
        return "%x" % x
    
    def sortlist(self,l):
        l = list(l)
        l.sort()
        return l



class LogXMLRPCRequestHandler(SimpleXMLRPCRequestHandler):
    protocol_version = "HTTP/1.1"
    def log_request(self, code='-', size='-'):
        """Log an accepted request.

        This is called by send_response().

        """

        self.log_message('"%s" "%s" %s %s',
                         str(self.client_address),self.requestline, str(code), str(size))    
    
class ThreadingServer(ThreadingMixIn,SimpleXMLRPCServer):
    pass    
server = ThreadingServer(('localhost',9000),LogXMLRPCRequestHandler,allow_none=True)
#server.set_server_title("Chapter 18 document")
#server.set_server_name("chapter")
#server.set_server_documentation("""welcome""")
server.register_instance(Math())
server.register_introspection_functions()
server.register_function(int)
server.register_function(list.sort)


try:
    print("Use Control-C to exit")
    server.serve_forever()
except KeyboardInterrupt:
    print("exiting")