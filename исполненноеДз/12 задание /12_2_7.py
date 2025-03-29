for i in range(1,46+1):
    for j in range(1,31+1):
            r = '1' * i  + '2' * j
            while '1111' in r:
                r = r.replace('1111', '2', 1)
                r = r.replace('222', '1', 1)
print(r)