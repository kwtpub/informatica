n = [int(x) for x in open('17.txt')]
k = 0
ans = []
z = []
for i in n: 
    if i % 100 == 25: 
        z.append(i)

minZ = min(z)


def ch(x): 
    if len(str(x)) == 2: 
        return 1 
    else: 
        return 0 

for i in range(0,len(n)-2):
    if (ch(n[i]) + ch(n[i+1]) + ch(n[i+2])) == 1 and n[i] + n[i+1] + n[i+2] < minZ: 
        ans.append(n[i] + n[i+1] + n[i+2])

print(len(ans), max(ans))
