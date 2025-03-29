from itertools import * 
k = 0
for i in product('ABCWXYZ', repeat=6):
    if i[0] in 'WXYZ' and i[5] in 'WXYZ':
        if i[1] not in 'WXYZ' and i[2] not in 'WXYZ' and i[3] not in 'WXYZ' and i[4] not in 'WXYZ':
            k += 1
print(k) #1296