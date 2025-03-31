from ipaddress import * 

def c(b): 
    return bin(b).count('1')

adress = ip_network('142.108.56.118/255.255.255.240',0)
k = 0 
for i in adress.hosts(): 
    p = list(i.packed)
    left = c(p[0]) + c(p[1]) 
    right = c(p[2]) + c(p[3])
    if left < right: 
        k += 1 
print(k)
