
import Queue,threading,time,random

 

class consumer(threading.Thread):
    def __init__(self,que):
        threading.Thread.__init__(self)
        self.daemon = False
        self.queue = que
    def run(self):
        while True:
            if self.queue.empty():
                break
            item = self.queue.get(timeout=0.1)
            #processing the item
            time.sleep(item/10)
            print self.name,item
            self.queue.task_done()
        return
que = Queue.Queue()
for x in range(10):
    que.put(random.random() * 10, True, None)
consumers = [consumer(que) for x in range(3)]

for c in consumers:
    c.start()
que.join()
print('ok')