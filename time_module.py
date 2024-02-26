import time

def using_for():
    for i in range(5000):
        print(i,end="")

def using_while():
    i=0
    while i < 5000:
        print(i,end="")
        i = i + 1

starting_time = time.time()
using_for()
end_time = time.time()-starting_time
print(f"Time taken by For loop: {end_time}")
starting_time = time.time()
using_while()
end_time = time.time()-starting_time
print(f"Time taken by While loop: {end_time}")