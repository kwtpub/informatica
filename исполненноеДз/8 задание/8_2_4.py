from itertools import * 
k = 0
for i in product('САЛО', repeat=6):
    n = ''.join(i)
    if 1 <= n.count('О') <= 3 :
        k += 1
print(k)