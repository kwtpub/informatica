k = 0

def m(x):
    return x.count(max(x)) == 1


for i in open('9.txt'):
    n = sorted(i.split())
    if m(n) and len(set(n)) == 4: 
        k += 1
        print(n)
print(k)
