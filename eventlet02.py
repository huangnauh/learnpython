from eventlet import hubs
from eventlet import greenthread
#from eventlet.support import greenlets as greenlet
def tellme(secret):
    print "a secret:",secret
    

#hub = hubs.get_hub()
#current = greenlet.getcurrent()
greenthread.spawn_n(tellme,"you are so beautiful")
#hub.schedule_call_global(0,tellme,"you are so beautiful")
#hub.switch()
greenthread.sleep(0)
print("ok")