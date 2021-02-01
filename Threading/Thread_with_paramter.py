
import threading

def runningCount(x):
    for i in range(x):
        print(threading.currentThread().getName(), " : ",i)
        


## runnning with this argument {It will run [MAIN-THREAD]}
# t = threading.Thread(target=runningCount(10), name="Thread #2")

# t.start()      ## -->   {This will run main Thread}

t2= threading.Thread(target=runningCount, name="Thread #2", args=(10,))

t2.start()