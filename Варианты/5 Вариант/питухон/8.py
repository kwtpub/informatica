from itertools import * 
k = 0
g = 0

for i in product('АВИОРТФ', repeat=6):
    n = ''.join(i) 
    k += 1
    if k % 2 == 0 and n[0] != 'О' and n.count('Р') == 2: 
        g += 1 
        print(n)

print(g,k)
