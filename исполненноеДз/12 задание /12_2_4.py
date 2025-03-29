for i in range(1,101):
    a = '1' + '9' * i
    while '19' in a or '299' in a or '3999' in a:
        if '19' in a:
            a = a.replace('19', '2', 1)
        elif '299' in a:
            a = a.replace('299', '3', 1)
        elif '3999' in a:
            a = a.replace('3999', '1', 1)
print(a)