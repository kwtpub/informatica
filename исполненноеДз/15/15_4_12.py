from itertools import *

def f(x,a1,a2):
    p = 257 <= x <= 1000
    q = 5 <= x <= 100
    r = 99 <= x <= 258
    a = a1 <= x <= a2
    return (a <= r) and ((not (a <= p)) <= q)

ox = [x/4 for x in range(3*4,1000*4)]
ans = []
for a1,a2 in combinations(ox,2):
    if all(f(x,a1,a2) for x in ox):
        ans.append(a2 - a1)