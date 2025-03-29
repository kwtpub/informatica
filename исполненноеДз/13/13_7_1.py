from ipaddress import * 

for i in range(0,33):
    address = ip_network(f'122.21.49.91/{i}',0)
    if str(address.network_address) == '122.21.48.0': 
        print(address) #20