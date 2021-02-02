import threading

# creating the {R-Entrant Lock } -> It can be acquired multiple times
lock = threading.RLock()

lock.acquire()

# The id are different for both the thread
print(id(lock.acquire))
print(id(lock.acquire()))

print("Helllo i am here")

# Its optional - {Work}
lock.release()

