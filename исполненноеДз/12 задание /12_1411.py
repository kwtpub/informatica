n = '1'*14 + '9992' * 33 + '9' + '2'*15
while '999' in n or '22' in n: 
    if '999' in n: 
        n = n.replace('999','12',1)
    else: 
        n = n.replace('22','1',1)
print(n.count('1'))

