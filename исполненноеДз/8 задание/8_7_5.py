from itertools import *
n = []
for i in product('АНП', repeat=5):
    f = ''.join(i)
    n.append(f)
n.sort()
print(n[200])