for a in range(4,10000+1):
    n = '1' + a*'2'
    while '12' in n or '3322' in n or '2222' in n: 
        if '12' in n: 
            n = n.replace('12','33',1)
        if '2222' in n: 
            n = n.replace('2222','1',1)
        if '3322' in n: 
            n = n.replace('3322','21',1)
    if  sum(map(int,n)) == 218: 
        print(a,n,sum(map(int,n)))
