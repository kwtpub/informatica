from itertools import * 

def f(x,a1,a2):
    c = 48 <= x <= 94 
    j = 83 <= x <= 100
    a = a1 <= x <= a2 
    return (not (c or j)) <= (not a)

ox = [x/4 for x in range(48*4,100*4)]
ans = [] 

for a1,a2 in combinations(ox,2):
    if all(f(x,a1,a2) for x in ox):
        ans.append(a2-a1)
print(max(ans)) #52