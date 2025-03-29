

n = [int(x) for x in open('17_1999.txt')]
asl = []
for i in range(0, len(n) - 2):
    if ((n[i] %12 == 0 or n[i+1] %12 == 0 or n[i+2] %12 == 0) and  
    n[i] %3 == 0 and n[i+1] %3 == 0 and n[i+2] %3 == 0):
        asl.append((n[i] + n[i+1] + n[i+2])/3)

print(len(asl))
print(min(asl))