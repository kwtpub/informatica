from itertools import * 

def f(x,a1,a2):
    p = 10 <= x <= 39 
    q = 23 <= x <= 58 
    a = a1 <= x <= a2 
    return (p and q) <= (q and a)

ox = [x/4 for x in range(10*4,60*4)]
ans =[]

for a1,a2 in combinations(ox,2):
    if all(f(x,a1,a2) for x in ox):
        ans.append(a2-a1)
print(min(ans)) #16