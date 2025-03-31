from itertools import * 
k = 0
for i in product('ЛОДКА', repeat=4):
    n = ''.join(i)
    if n.count('О') >= 2:
        k += 1
print(k) #113
