for i in range(1, 85+1):
    a = '9' * i
    while '666'in a or '999'in a:
        if '666' in a:
            a = a.replace('666', '9', 1)
        else:
            a = a.replace('999', '6', 1)
print(a)
