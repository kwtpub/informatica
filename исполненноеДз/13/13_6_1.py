from ipaddress import * 
k = 1
for i in range(1,32):
    address = ip_network(f'98.162.71.94/255.255.255.192',0)
    k += 1
    if str(address.network_address) == '98.162.71.64':
        print(address.netmask)
    print(k) #32