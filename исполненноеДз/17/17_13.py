n = [int(x) for x in open('17/17_2401.txt')]
ans = []
for i in range(len(n) - 1):
    if 50 <= abs(n[i]) + abs(n[i+1]) <= 200: 
        s = n[i],n[i+1]
        ans.append(s)
print(len(ans))
print(min(ans))