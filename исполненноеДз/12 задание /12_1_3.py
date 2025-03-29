for i in range(1,1000+1):
    n = '8' * i
    while '999' in n or '888' in n:
        if '888' in n:
            n = n.replace('888', '9', 1)
        else:
            n = n.replace('999', '8', 1)
print(n)

