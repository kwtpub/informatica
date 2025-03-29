from functools import * 
from math import * 

# @lru_cache(None)

# def F(n):
#     if n == 1: return 1 
#     else: return n * F(n - 1)

# for i in range(2,2200):
#     F(i)

f1 = factorial(2024)
f2 = factorial(2023)
f3 = factorial(2022)

res = (f1 // 4 + f2) // f3
print(res)