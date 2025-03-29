from sys import *
from functools import *
setrecursionlimit(100000000)
@lru_cache(None)



def f(n):
    if n <= 1: 
        return n
    elif n >1 and n%3==0: 
        return n + f(n/3)
    elif n >1 and n%3!=0: 
        return n + f(n + 3)



for i in range(1,100):
    try:
        if f(i) > 100: print(i)
    except:
        ...