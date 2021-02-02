import threading

x = 0
def running():
    global x
    for _ in range(100000):
        x += 1

t1= threading.Thread(target=running, name="Thread #1")
t2= threading.Thread(target=running, name="Thread #2")

t1.start()
t2.start()

# Joinning the thread as the work is done in a regular order 
t1.join()
t2.join()

#printing the value of x after increasing the counter
print("Value of x : ",x)
