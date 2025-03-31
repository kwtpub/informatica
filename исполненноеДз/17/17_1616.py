n = [int(x) for x in open('17/17.16_14653.txt')]
ans = []
mn1 = min([x for x in n if x % 17 == 0 and x>0]) 
mn2 = min([x for x in n if x % 17 == 0 and x>0 and x!= mn1])  
mx69 = max([x for x in n if abs(x) % 100 == 69]) 
for i in range(len(n)-3):
    if ((len(str(abs(n[i]))) == 3 + len(str(abs(n[i+1]))) == 3 + len(str(abs(n[i+2]))) == 3 + len(str(abs(n[i+3]))) == 3) == 2 and
    (abs(n[i]) % 18 == 0 + abs(n[i+1]) % 18 == 0 + abs(n[i+2]) % 18 == 0 +  abs(n[i+3]) % 18 == 0) == 1 and 
    (n[i] + n[i+1] + n[i+2] + n[i+3]) % (mn1 + mn2) == 0 and
    (n[i]*n[i+1]*n[i+2]*n[i+3]) <= mx69**2):
        ans.append((n[i]+n[i+1]+n[i+2]+n[i+3])**2)
print(len(ans), min(ans))

