
n = [int(x) for x in open('17/17_2403.txt')]
ans = []
for i in range(len(n)-1):
    n1 = n[i]
    n2 = n[i+1]
    if n2 % 9 != 0 and n1 % 9 == 0 and int(oct(abs(n2))[2:]) % 10 == 3 or n1 % 9 != 0  and n2 % 9 == 0 and int((oct(abs(n1))[2:])) % 10 == 3:
        ans.append(max(n1,n2))
print(len(ans))
print(max(ans))
