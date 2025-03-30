k = 0
for x in open('9.txt'):
    n = sorted([int(z) for z in x.split()])
    if n[3] < n[2] + n[1] + n[0] and len(set(n)) == 3:
        k += 1 
print
    