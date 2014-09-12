#!E:/python27/python.exe
# -*- coding: utf-8 -*-

import asyncore, socket
import threading

#收到data最大長度
MAX_RECV = 4096

#連線server的socket
class client(asyncore.dispatcher):

   def __init__(self, host, port):
       asyncore.dispatcher.__init__(self)
       self.SendData = ""
       self.RecvData = ""
       #和server建立連線
       self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
       self.connect( (host, port) )

   def handle_connect(self):
       print 'connect!!'

   def handle_close(self):
       print "disconnection : " + self.getpeername()[0]
       self.close()

   #收到的data
   def handle_read(self):
       self.RecvData = self.recv(MAX_RECV)
       if len(self.RecvData) > 0:
           print "recv : " + self.RecvData

   #送出data
   def handle_write(self):
       send_byte = self.send(self.SendData)
       if send_byte > 0:
           send_out = self.SendData[:send_byte]
           self.SendData = self.SendData[send_byte:]
           print "send : " + send_out
           self.handle_write()
       else:
           print "send all!!"
           self.SendData = ""
   #自動偵測送出永遠失敗
   def writable(self):
       print "writable"
       return False
  
#等待server傳送訊息的thread
class send_server_thread(threading.Thread):
   def __init__(self,host,port):
       self.client = client(host, port)
       threading.Thread.__init__ ( self )
   def run(self):
       try:
           asyncore.loop()
       except:
           pass
#等待user input的thread       
class input_thread(threading.Thread):
   def __init__(self,client_thread):
       self.client_thread = client_thread
       threading.Thread.__init__ ( self )
   def run(self):
       while 1:
           send_data = raw_input()
           self.client_thread.client.SendData = send_data
           self.client_thread.client.handle_write()

#主程式
if __name__ == "__main__":
   #建立和server連線, 並且等待溝通
   client_thread = send_server_thread("localhost",111)
   client_thread.start()
   #等待user input
   input_thread(client_thread).start()