from functools import * 
@lru_cache(None)
def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 3
    elif n>1:
        return f(n-1) -f(n-2) + 3*n
    
print(f(40))