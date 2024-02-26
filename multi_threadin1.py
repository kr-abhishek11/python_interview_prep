import threading
import time

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

# normal code
func(4)
func(2)
func(1)
time1 = time.perf_counter()
print(f"Time taken by normal function {time.perf_counter()- time1}")

# Using multithreading
time2= time.perf_counter()
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print(f"Time taken by using multithreading {time.perf_counter()-time2}")