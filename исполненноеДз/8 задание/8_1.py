from itertools import *
k = 0
for i in product('12345', repeat=5):
    n = ''.join(i)
    if n.count('1') == 3:
        k += 1
print(k)