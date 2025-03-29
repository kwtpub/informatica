from ipaddress import * 

address = ip_network('0.0.0.0/255.255.254.0', 0 )

print(len(list(address.hosts())))