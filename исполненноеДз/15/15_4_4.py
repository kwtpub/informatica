from itertools import * 

def f(x,a1,a2):
    p = 5 <= x <= 30
    q = 14 <= x <= 23
    a = a1 <= x <= a2
    return (p == q) <= (not a)

ox = [x/4 for x in range(3*4,33*4)]
ans = []

for a1, a2 in combinations(ox,2):
    if all(f(x,a1,a2) for x in ox):
        ans.append(a2-a1)
print(max(ans)) #9