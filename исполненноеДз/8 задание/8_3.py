from itertools import * 
k = 0
for i in product('МИКРЯ', repeat=8):
    n = ''.join(i)
    if n.count('М') == 2 and n.count('И') == 3 and n.count('К') == 1 and n.count('Р') == 1 and n.count('Я') == 1:
        k += 1
print(k)
