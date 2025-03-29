from ipaddress import * 

for x in range(0,32): 
    address = ip_network(f'224.128.114.142/19', 0)
    print(str(address.netmask))
    # if str(address.hosts()) == '224.128.96.0':
    #     print(address.netmask()) 224