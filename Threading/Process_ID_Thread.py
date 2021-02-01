
import threading
import os

def runningCount(x):
    for i in range(x):
        print(threading.currentThread().getName(), " : ",i)
        print(os.getpid())

## --------------------##

t2= threading.Thread(target=runningCount, name="Thread #2", args=(10,))
t2.start()

t3= threading.Thread(target=runningCount, name="Thread #3", args=(10,))
t3.start()