a = '2' + '5' * 81
while '25' in a or '355' in a or '4555' in a:
    if '25' in a:
        a = a.replace('25', '4', 1)
    elif '355' in a:
        a = a.replace('355', '2', 1)
    elif '4555' in a:
        a = a.replace('4555', '3', 1)
print(a)
