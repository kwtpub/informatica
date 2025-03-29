from itertools import * 
k = 0
for i in product('012345678', repeat=5):
    n = ''.join(i)
    n = n.replace('1', '7').replace('3', '7').replace('5', '7')
    if n[0] != "0" and n.count('0')== 1 and '07' not in n and '70' not in n:
         k += 1 
print(k)
