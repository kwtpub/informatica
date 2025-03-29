n = [int(x) for x in open('17/17_2400.txt')]
ans = []
for i in range(0, len(n) - 1):
    if n[i] + n[i+1] >= 100 and (n[i] < 0 or n[i+1] < 0):
        ans.append(n[i] * n[i+1])
print(len(ans))
print(max(ans))
