#!E:/python34/python.exe
#coding= utf-8
import logging
from http.server import CGIHTTPRequestHandler
from xmlrpc.server import SimpleXMLRPCServer,SimpleXMLRPCDispatcher,CGIXMLRPCRequestHandler
class MyFuncs:
    def mul(self, x, y):
        return x * y

server.register_function(pow)
server.register_function(lambda x,y: x+y, 'add')
server.register_introspection_functions()
server.register_instance(MyFuncs())
server.handle_request()

