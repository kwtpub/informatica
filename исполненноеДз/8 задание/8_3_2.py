from itertools import *
k = 0
for i in product('НИКОЛАЙ', repeat=4):
    n = ''.join(i)
    print(n)
    if n[0] != 'Й' and 'ИАО' in n:
        
        k += 1
print(k) # 13