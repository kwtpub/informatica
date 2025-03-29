from ipaddress import * 
address = ip_network('10.48.96.0/255.255.240.0',0)
k = 0
for i in address: 
    if bin(int(i))[2:].count('1') > 16:
        k += 1
        print(k)