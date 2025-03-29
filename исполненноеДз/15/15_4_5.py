from itertools import * 

def f(x,a1,a2):
    p = 10 <= x <= 40
    q = 5 <= x <= 15
    r = 35 <= x <= 50
    a = a1 <= x <= a2
    return (a or p) or (q <= r)

ox = [x/4 for x in range(3*4, 55*4)]
ans = []

for a1,a2 in combinations(ox, 2):
    if all(f(x,a1,a2) for x in ox):
        ans.append(a2-a1)
print(min(ans)) #5