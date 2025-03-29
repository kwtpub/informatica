n = '9' * 100
while '33333' in n or '999' in n:
    if '33333' in n:
        n = n.replace('33333','99', 1)
    else:
        n = n.replace('999','3', 1)
print(n)