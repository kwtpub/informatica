from itertools import * 
k = 0
for i in product('ТИМОФЕЙ', repeat=5):
    n = ''.join(i)
    if n.count('Т') >= 1 and n.count('Й') <= 1:
        k += 1 
print(k)