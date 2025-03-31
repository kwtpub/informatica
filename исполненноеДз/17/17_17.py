n = [int(x) for x in open('17/17_2310.txt')]
ans1 = []
ans2 = []
for i in range(len(n)):
    if abs(n[i]) % 10 == 4:
        ans1.append(n[i])
z = max(ans1) + min(ans1)
for j in range(len(n)-1):
    if n[j] + n[j+1] < z:
        ans2.append(n[j] + n[j+1])
print(len(ans2))
print(max(ans2))
