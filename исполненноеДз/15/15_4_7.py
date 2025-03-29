from itertools import * 

def f(x,a1,a2):
    d = 17 <= x <= 58 
    c = 29 <= x <= 80
    a = a1 <= x <= a2 
    return d <= (((not c) and (not a)) <= (not d))

ox = [x/4 for x in range(15*4,85*4)]
ans = []
for a1,a2 in combinations(ox,2):
    if all(f(x,a1,a2) for x in ox):
        ans.append(a2-a1)
print(min(ans)) #12