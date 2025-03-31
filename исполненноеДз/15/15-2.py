from itertools import *

def f(x,a1,a2):
    p = 25 <= x <= 50
    q = 32 <= x <= 47 
    a = a1 <= x <= a2
    return ((not a) <= p) <= (a <= q)

ox = [x/4 for x in range(24*4,51*4)]
ans = []

for a1,a2 in combinations(ox,2):
    if all(f(x,a1,a2) for x in ox):
        ans.append(a2 -a1)
print(max(ans))