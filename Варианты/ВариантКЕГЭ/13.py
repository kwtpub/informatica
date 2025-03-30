from ipaddress import * 

address = ip_network('172.16.80.0/255.255.248.0', 0)

k = 1
for i in address.hosts(): 

    octets = str(i).split('.')

    countOne = [bin(int(oct)).count('1') for oct in octets ]
    if sum(countOne) % 2 != 0: 
        k += 1 

print(k)