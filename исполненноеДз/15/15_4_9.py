from itertools import * 

def f(x,a1,a2):
    b = 18 <= x <= 52 
    c = 16 <= x <= 41
    a = a1 <= x <= a2
    return (b <= a) and ((not c) or a)

ox = [x/4 for x in range(16*4,54*4)]
ans = []

for a1,a2 in combinations(ox, 2):
    if all(f(x,a1,a2) for x in ox):
        ans.append(a2-a1)
print(min(ans)) #36 