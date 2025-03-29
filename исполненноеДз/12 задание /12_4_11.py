n = '>' + 26*'1' + 10*'2' + 14*'3'
while '>1' in n or '>2' in n or '>3' in n:
    if '>1' in n:
        n = n.replace('>1','22>',1)
    elif '>2' in n:
        n = n.replace('>2','2>',1)
    elif '>3' in n:
        n = n.replace('>3','1>',1)
print(sum(map(int, n[:-1])))