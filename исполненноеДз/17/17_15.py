n = [int(x) for x in open('17/17_2239.txt')]
ans1 = []
ans2 = []
for z in range(len(n)-1):
    if n[z] % 19 == 0:
        ans1.append(n[z])
for i in range(len(n)-1):
    if  ((n[i] > max(ans1)) + (n[i+1] > max(ans1))) >= 1:
        ans2.append(n[i] + n[i+1])
print(len(ans2))
print(min(ans2))