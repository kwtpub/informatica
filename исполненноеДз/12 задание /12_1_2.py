for i in range(1,125+1):
    a = '8' * i
    while '333' in a or '888' in a:
        if '333' in a:
            a = a.replace('333', '8', 1)
        else:
            a = a.replace('888', '3', 1)
print(a)