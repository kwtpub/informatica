from itertools import * 

def f(x,a1,a2):
    p = 14 <= x <= 58
    q = 29 <= x <= 80 
    a = a1 <= x <= a2
    return p <= ((q and (not a)) <= (not p))

ox = [x/4 for x in range(14*4, 82*4)]
ans = []

for a1,a2 in combinations(ox,2):
    if all((f(x,a1,a2) == 1 for x in ox)):
        ans.append(a2 - a1)
    
print(min(ans))