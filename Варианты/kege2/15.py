def Дел(n,m):
    if m == 0:
        return 0
    if abs(n) % abs(m) == 0:
        return 1
    else:
        return 0
def Дел2(n,m):
    if m == 0:
        return 1
    if abs(n) % abs(m) == 0:
        return 0
    else:
        return 1
B = [int(i) for i in range(71,91)]
x = 30
    

for x in range(0,200):
        for A in range(0,200):
            if Дел(x,A) or (int(x in B) <= Дел2(x,22)) == 1:
                 print(A)