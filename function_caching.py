"""
Memoize - to store (the result of a computation) so that it can be subsequently retrieved without repeating the computation
"""

import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(2))
print("Done for 2")
print(fx(4))
print("Done for 4")
print(fx(6))
print("Done for 6")

print(fx(2))
print("Done for 2")
print(fx(4))
print("Done for 4")
print(fx(6))
print("Done for 6")

