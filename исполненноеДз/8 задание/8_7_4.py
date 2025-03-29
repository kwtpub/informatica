from itertools import *
n = []
for i in product('ЛНРТ', repeat=5):
    f = ''.join(i)
    n.append(f)
n.sort()
print(n[149])