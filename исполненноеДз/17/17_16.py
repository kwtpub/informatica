n = [int(x) for x in open('17/17_2309.txt')]
ans11 = []
ans17 = []
for i in range(len(n)):
    if n[i] % 11 == 0:
        ans11.append(n[i])
    if n[i] % 17 == 0:
        ans17.append(n[i])
if len(ans11) > len(ans17):
    print(len(ans11))
    print(min(ans11))
else:
    print(len(ans17))
    print(min(ans17))