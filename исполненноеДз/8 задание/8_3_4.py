from itertools import * 
k = 0 
for i in product('ВИКТОР', repeat=4):
    n = ''.join(i)
    if all(n.count(x) <= 1 for x in 'ВИКТОР'):
        n = n.replace('В', 'i').replace('К', 'i').replace('Т', 'i').replace('Р', 'i')
        n = n.replace('И', '2').replace('О', '2')
        if n[0] != n[1] != n[2] != n[3]:
            k += 1

print(k) ##?

