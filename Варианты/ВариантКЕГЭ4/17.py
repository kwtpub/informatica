n = [int(x) for x in open('17.txt')]

ans = []
minnum = min(n)

for i in range(len(n)-1):
    if n[i] % 16 == minnum or n[i+1] % 16 == minnum:
        ans.append(n[i] + n[i+1])

print(max(ans), len(ans))
