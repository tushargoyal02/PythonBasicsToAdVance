
import threading

#know the name of the thread - {This is our [MainThread]}
print(threading.current_thread().getName() )

def functionThread():
    for i in range(12):
        print(threading.current_thread().getName() , i)

#creating the first thread - {Target => What to exectute }
#{name : Is the name you give to your thread}

thread1 = threading.Thread(target=functionThread, name='ThreadCreatead1')
thread2 = threading.Thread(target=functionThread, name='ThreadCreatead2')

thread1.start()
thread2.start() 