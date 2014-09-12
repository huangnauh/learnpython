#!/usr/bin/env python
# coding: utf-8

import socket
import select
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("",8080))
sock.listen(5)

ins = [sock]
outs = []
excs = []
addrs = {}
data = {}
try:
    while True:
        i,o,e = select.select(ins,outs,excs)
        for x in i:
            if x is sock:
                client,addr = sock.accept()
                print "Connected from " , addr
                ins.append(client)
                addrs[client] = addr
            else:
                newdata = x.recv(1024)
                if newdata:
                    print "%d bytes from %s" % (len(newdata),addrs[x])
                    data.setdefault(x,[]).append(newdata)
                    print(data[x])
                    if x not in outs:
                        outs.append(x)
                else:
                    print "disconnected from", addrs[x]
                    del addrs[x]
                    try:
                        outs.remove(x)
                    except ValueError:
                        pass
                    x.close()
                    ins.remove(x)
        for x in o:
            senddata = data.get(x)
            print(1,senddata)
            if senddata:
                senddata = "".join(senddata)
                nsent = x.send(senddata)
                print "%d bytes to %s" % (nsent,addrs[x])
                senddata = senddata[nsent:]
            if senddata:
                print "%d types remain for %s" % (len(senddata),addrs[x])
                data[x] = [senddata]
            else:
                try:
                    del data[x]
                except KeyError:
                    pass
                outs.remove(x)
                print "No data currenly remain for",addrs[x]
finally:
    sock.close()

