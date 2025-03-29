a = '1' + '0' * 33
while '1' in a or '100' in a:
    if '100' in a: 
        a = a.replace('100', '0001', 1)
    else:
        a = a.replace('1', '00')
print(a.count('0'))