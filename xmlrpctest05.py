import xmlrpclib,sys,code
import httplib
import threading
url = "http://localhost:9000"
#url = 'http://localhost:9000/cgi-bin/cgi108.py'
class KeepAliveTransport(xmlrpclib.Transport):
    def make_connection(self, host):
        #return an existing connection if possible.  This allows
        #HTTP/1.1 keep-alive.
        if self._connection and host == self._connection[0]:
            return self._connection[1]

        # create a HTTP connection object from a host descriptor
        chost, self._extra_headers, x509 = self.get_host_info(host)
        if self._extra_headers is None:
            self._extra_headers = [("Connection","Keep-Alive")]
        elif isinstance(_extra_headers,list):
            self._extra_headers.append(("Connection","Keep-Alive"))
        #store the host argument along with the connection object
        self._connection = host, httplib.HTTPConnection(chost)
        return self._connection[1]
        

def interact():
    interp = code.InteractiveConsole({'proxy':proxy})
    interp.interact("you can now use the object proxy to interact with the server")

def test2():
    methods = proxy.system.listMethods()
    while 1:
        print "\n\nAvailable Methods"
        for i in range(len(methods)):
            print "%2d: %s" % (i+1,methods[i])
        selection = raw_input('select one (q to quit):')
        if selection == 'q':
            break
        item = int(selection)-1
        print "\n***"
        print "Details for %s\n" % methods[item]
        print "Help:",proxy.system.methodHelp(methods[item])

def test():
    proxy = xmlrpclib.ServerProxy(url,transport=KeepAliveTransport())
    for i in xrange(10):
        proxy.pow(i,i)
#        print("%s:pow(%d,%d)=%d" % (str(threading.currentThread()),i,i,proxy.pow(i,i)))
#        print("%s:hex(%d)=%s" % (str(threading.currentThread()),i,proxy.hex(i)))
    print('%s:stats:%s' % (str(threading.currentThread()),str(proxy.getstats())))
#    print('%s:stats:%s' % (str(threading.currentThread()),str(proxy.getruntime())))

for i in range(20):
    threading.Thread(target=test).start()