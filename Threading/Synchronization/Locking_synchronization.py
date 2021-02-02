import threading

x = 0

# creating a thread lock here
lock = threading.Lock()

def running():
    global x
    for _ in range(100000):

        #acquire a lock
        lock.acquire()

        # This works as a {CRITICAL SECTION}
        x += 1

        #releasing a lock - For other thread to work
        lock.release()

t1= threading.Thread(target=running, name="Thread #1")
t2= threading.Thread(target=running, name="Thread #2")

t1.start()
t2.start()

# Joinning the thread as the work is done in a regular order 
t1.join()
t2.join()

#printing the value of x after increasing the counter
print("Value of x : ",x)
