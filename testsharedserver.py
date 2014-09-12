#!/usr/bin/env python
# -*- coding: UTF8 -*-
import time
import threading
import thread
import SocketServer
 
from multiprocessing import Manager
 
 
class AppHandler(SocketServer.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
 
    def setup(self):
        print("%s is connected!" % self.client_address[0])
        yes = Application.yes
        yes[self.client_address[0]] = self.client_address[0]
        self.test = yes[self.client_address[0]]
 
    def handle(self):
        while True:
            try:
                recv = self.request.recv(10)
                print self.test
                print recv[2]  
# if clinet close this is a Exception and goto Exception
            except Exception, e:
                print (e)
                self.request.send("error")
                break
 
    def finish(self):
        yes = Application.yes
        yes[self.client_address[0]] = None
        print("%s disconnected." % self.client_address[0])
 
 
class AppServer(SocketServer.ThreadingTCPServer):
    stopped = False
    allow_reuse_address = True
 
    def __init__(self, server_address, RequestHandlerClass):
        print "server start init"
        SocketServer.ThreadingTCPServer.__init__(self, server_address, RequestHandlerClass)
 
    def serve_forver(self):
        while not self.stopped:
            self.handle_request()
 
    def stop(self):
        self.stopped = True
        self.shutdown()
        self.socket.close()
 
    def verify_request(self, request, client_address):
        return True
 
    def close_request(self, request):
        print("%d" % thread.get_ident())
 
 
class Application():
 
    thread = None
    server = None
    manager = None
    yes = None
 
    def __init__(self, ip, port):
        self.port = port
        self.ip = ip
 
    def startup(self):
        print("Application startup ...")
        try:
            Application.manager = Manager()
            Application.yes = Application.manager.dict()
            Application.server = AppServer((self.ip, self.port), AppHandler)
            Application.thread = threading.Thread(name="Application server", target=Application.server.serve_forever)
            Application.thread.start()
        except Exception, e:
            print(e)
        finally:
            while True:
                print "while"
                print Application.yes
                time.sleep(3)
 
    def shutdown(self):
        print("Application shutdown ...")
        try:
            Application.server.stop()
        except Exception, e:
            print(e)
 
        time.sleep(1)
 
 
if __name__ == "__main__":
    ip = ""
    port = 6002
    app = Application(ip, port)
    app.startup()