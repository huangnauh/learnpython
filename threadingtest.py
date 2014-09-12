# encoding: UTF-8
import threading
import time

class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)
        num += 1
        msg = self.name+' set num to '+str(num)
        print msg
num = 0
mutex = threading.Lock()    
if __name__ == '__main__':
    threads = []
    for i in range(20):
        t = MyThread()
        threads.append(t)
        t.start()
    for i in threads:
        i.join()
    print(num)
    