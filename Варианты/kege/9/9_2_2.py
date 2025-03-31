k = 0 
for s in open('kege/9/9_2_2.txt'):
    
    n = sorted([int(x) for x in s.split()])
    n4 = [x for x in n if n.count(x) == 4]    
    n1 = [x for x in n if n.count(x) == 1]    
    if len(n4) == 4 and len(n1) == 3 and n4[0] < sum(n)/len(n):
        k +=  1 
print(k) #10