import random, threading, time
from scj.code.snapshot import new_snapshot
from queue import Queue
class StoreSnapshot(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        while(True):
            val = self.data.get()
            if val[0] is None and val[1] is None:
                break
            else:
                new_snapshot(val[0],val[1])