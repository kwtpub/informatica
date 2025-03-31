for x in range(1,50): 
    for y in range(1,50):
        for z in range(1,50):
            n = '0'+ '1'*x + '2'*y + '3'*z + '0'
            while '00' not in n:
                n = n.replace('01', '210', 1)
                n = n.replace('02', '3101', 1)
                n = n.replace('03', '2012', 1)

            if n.count('1') == 70 and n.count('2') == 56 and n.count('3') == 23:
                print(sum((int(x), int(y),int(z)))+ 2)