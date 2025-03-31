from ipaddress import * 

for mask in range(32):
	address1 = ip_network(f'172.16.0.2/{mask}', 0)
	address2 = ip_network(f'151.115.79.61/{mask}', 0)
	if str(address1) == str(address2):
		print(address1, 'and', address2)