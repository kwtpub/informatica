from itertools import *
n = []
k = 1
for i in product('МАРИЯ', repeat=4):
    f = ''.join(i)
    n.append(f)
    k += 1
n.sort()
print(n[210])
