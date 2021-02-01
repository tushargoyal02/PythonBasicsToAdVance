import threading

print(threading.current_thread().getName() )

def functionThread():
    for i in range(12):
        print(threading.current_thread().getName() , i)

thread1 = threading.Thread(target=functionThread, name='t1')
thread2 = threading.Thread(target=functionThread, name='t2')

thread1.start()
thread2.start() 

thread1.join()
thread2.join()

print("### ---- THE MAIN THREAD WILL EXECUTE THIS IN BETWEEN ---- ####")




