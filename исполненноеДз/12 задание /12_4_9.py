for x in range(1,50):
    for y in range(1,50):
        for z in range(1,50): 
            n = '0' + '1'*x + '2'*y + '3'*z
            while '01' in n or '02' in n or '03' in n:
                n = n.replace('01','302',1)
                n = n.replace('02','3103',1)
                n = n.replace('03','20',1)
            if n.count('1') == 28 and n.count('2') == 34 and n.count('3') == 45:
                print(x)