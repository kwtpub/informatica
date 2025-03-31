for i in range(1,70+1):
    a = '8' * i
    while '2222' in a or '8888' in a:
        if '2222' in a:
            a = a.replace('2222', '88', 1)
        else:
            a = a.replace('8888', '22', 1)
print(a)

