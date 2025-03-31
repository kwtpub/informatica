n = [int(x) for x in open('kege2/17.txt')]
ans =[]
ans2=[]
for j in range(len(n)):
    if n[j] % 32 == 0:
        ans.append(n[j])
for i in range(len(n)-1):
    n1 = n[i]
    n2 = n[i+1]
    if ((abs(n1) != n1) + (abs(n2) != n2) >= 1) and  (n1 +n2) < len(ans):
        ans2.append(n1 + n2)
print(len(ans2), max(ans2))