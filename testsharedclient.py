#!/usr/bin/env python
# -*- coding: UTF8 -*-
import socket
import time
import sys
 
HOST = '127.0.0.1'  
# The remote host
PORT = 6002  
# The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    s.send('world!')
    
#data = s.recv(1024)
    
#print 'Received', repr(data)
    time.sleep(1)
s.close()   