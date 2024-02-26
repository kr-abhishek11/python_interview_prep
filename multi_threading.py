"""
A thread is a subset of the process.
Multithreading is defined as the ability of the processor to execute multiple threads concurrently.
In a single-core CPU, it is acheived using frequent switching between threads. This is termed as 
"Context Switching", the state of the thread is saved and the state of another thread is loaded whenever ny interrupt (due to I/O or manully)
tkes place.. Context switching takes place so frequently that all the threads appear to be running parallely (this is termed as multi tasking)
"""

import threading

def print_cube(num):
    print(f"Cube :{num*num*num}")

def print_square(num):
    print(f"Square: {num*num}")

if __name__ == "__main__":
    t1 = threading.Thread(target=print_cube,args=(10,)) # creating a thread
    t2 = threading.Thread(target=print_square,args=(10,))

    t1.start() # starting a thread
    t2.start()

    t1.join()# ending the thread execution
    t2.join()

    print("DOne!")