from ipaddress import * 
address = ip_network('210.66.110.0/255.255.252.0', 0)
k = 0
for ip in address:
    k = bin(int(ip))[2:].count('1') 
    if k % 6 != 0: 
        k += 1
print(k)
