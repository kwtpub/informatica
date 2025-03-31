n = [int(x) for x in open('17var03.txt')]

minN = min(n)
ans = []
for i in range(1,len(n)-1):
    if ((n[i] % 44) + (n[i+1] % 44)) == minN:
        ans.append(abs(n[i] - n[i-1]))

print(len(ans), min(ans))

