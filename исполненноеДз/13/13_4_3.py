from ipaddress import * 

address = ip_network('0.0.0.0/255.255.255.128',0)
k = 0 
for i in address.hosts():
    k += 1 

print(k) #126