from ipaddress import *  

for i in range(0,32+1): 
    address = ip_network(f'117.191.88.37/20', 0)
    print(address.netmask)#240