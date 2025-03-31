n = '1' + '0' * 90

while '1' in n:
    if '10' in n: 
        n = n.replace('10', '0001', 1)
    else: 
        n = n.replace('1', '000',1)
    
print(n.count('0'))
    