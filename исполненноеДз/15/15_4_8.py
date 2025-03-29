from itertools import * 

def f(x,a1,a2):
    p = 17 <= x <= 54
    q = 37 <= x <= 83 
    a = a1 <= x <= a2 
    return p <= ((q and (not a)) <= (not p))

ox = [x/4 for x in range(17*4,83*4)]
ans = []

for a1,a2 in combinations(ox,2):
    if all(f(x,a1,a2) for x in ox):
        ans.append(a2-a1)
print(min(ans)) #17

