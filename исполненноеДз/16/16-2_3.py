from functools import *

@lru_cache(None)



def f(n):
    if n > 100000:
        return n
    if n <= 100000:
        return f(n+1) + 5*n + 2 

for i in range(100000, 1, -1): 
        f(i)

print(f(3) - f(7))