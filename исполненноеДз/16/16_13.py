from functools import *

@lru_cache(None)
def f(n):
    if n <= 18: return n + 3 
    elif n % 3 == 0:
        return (n//3) * f(n//3) + n -12
    elif n % 3 != 0:
        return f(n-1) + n**2 + 5 
k = 0 
for i in range(1,1001):
    a = f(i)
    if all(int(b)%2==0 for b in str(a)):
        k += 1 
print(k)