from ipaddress import * 

address = ip_network('206.158.124.67/255.255.224.0', 0)
k = 1
for i in address.hosts():
    if str(i) == '206.158.124.67':
        print(k)
    k += 1 #7235