from time import perf_counter

def sample():
    for i in range(20):
        print(i)

time_before = perf_counter()
sample()
time_after = perf_counter() - time_before
print(time_after)