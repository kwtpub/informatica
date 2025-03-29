n = [int(x) for x in open('17/17_2398.txt')]
ans = []

for i in range(len(n)-2):
    k1 = not(n[i])
    if ((n[i+1] > 0 and abs(n[i+1]) % 10 == 9) :

        ans.append(n[i] + n[i+1] + n[i+2])
print(len(ans), max(ans)) ##???