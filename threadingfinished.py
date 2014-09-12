import threading
from multiprocessing import Process, Event
from time import sleep

def childsPlay(event):
    print "Child started"
    for i in range(3):
        print "Child is playing..."
        sleep(1)
    print "Child done"
    event.set()

def endlessChildsPlay(event):
    print "Endless child started"
    while True:
        print "Endless child is playing..."
        sleep(1)
        event.set()
    print "Endless child done"

class ChildChecker(threading.Thread):
    def __init__(self, killEvent):
        super(ChildChecker, self).__init__()
        self.killEvent = killEvent
        self.event = Event()
        self.process = Process(target=childsPlay, args=(self.event,))

    def run(self):
        self.process.start()

        while not self.killEvent.is_set():
            self.event.wait()
            print "Child checked, and is done playing"
            if raw_input("Do again? y/n:") == "y":
                self.event.clear()
                self.process = Process(target=endlessChildsPlay, args=(self.event,))
                self.process.start()
            else:
                self.cleanChild()
                self.killEvent.set()

    def join(self):
        print "Joining child process"
        # Timeout on 5 seconds
        self.process.join(5)

        if self.process.is_alive():
            print "Child did not join!  Killing.."
            self.process.terminate()
        print "Joining ChildChecker thread"
        super(ChildChecker, self).join()


    def cleanChild(self):
        print "Cleaning up the child..."

if __name__ == '__main__':
    killEvent = Event()
    # thread to check on child process
    t = ChildChecker(killEvent)
    t.start()

    try:
        while not killEvent.is_set():
            print "GUI running..."
            sleep(1)
    except KeyboardInterrupt:
        print "Quitting..."
        exit(0)
    finally:
        t.join()
        print "Main done"