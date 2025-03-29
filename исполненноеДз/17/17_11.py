n = [int(x) for x in open('17/17_2002.txt')]
ans = []
for i in range(0, len(n)-3):
    if n[i] > n[i+1] > n[i+2] > n[i+3] and ((n[i] - n[i+3]) > 1000):
        ans.append(n[i] + n[i+1] + n[i+2]+ n[i+3])
print(len(ans))
print(min(ans))
