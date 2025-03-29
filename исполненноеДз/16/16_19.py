from functools import *
@lru_cache(None)
def f(n):
    if n < 3:
        return n +1 
    elif n >=3 and n%3==0:
        return f(n-2) + n -2
    elif n >= 3 and n%3!=0:
        return f(n+2) + n + 2
k = 0 
for i in range(1,1000):
    try:
        if 10000 <= f(i) < 1000000: k+=1
    except:
        ...

print(k)