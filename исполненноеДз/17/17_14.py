n = [int(x) for x in open('17/17_2238.txt')]
ans = []
z = sum(n) / len(n)
for i in range(len(n)- 2 ):
    n1 = n[i]
    n2 = n[i+1]
    n3 = n[i+2]
    if ((n1>z) + (n2>z) + (n3>z)) >= 2:
        ans.append(n1 +n2 +n3)
print(len(ans))
print(max(ans))
"""if ((n1 > z and n2 > z and n3 < z) or 
    (n1 < z and n2 > z and n3 > z) or
    (n1 > z and n2 < z and n3 > z) or
    (n1 > z and n2 > z and n3 > z) or 
    (n1 > z and n2 > z and n3 > z) or
    (n1 > z and n2 > z and n3 > z)
    ):"""

