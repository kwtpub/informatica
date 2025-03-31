from functools import *

@lru_cache(None)

def f(n): 
    if n == 1:
        return 1 
    else: 
        return n + f(n - 1)

for i in range(1,3500):
    f(i)
print(f(3000) - f(2000))
