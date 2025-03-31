from ipaddress import *

#13_2
print('Ответ 13_2:', end = " ")
address = ip_network('217.9.142.131/255.255.192.0', 0)
print(address)


#13_2_1
print('Ответ 13_2_1:', end = " ")
address = ip_network('146.212.200.55/255.255.240.0', 0)
print(address)


#13_2_2
print('Ответ 13_2_2:', end = " ")
address = ip_network('224.24.254.134/255.255.224.0', 0)
print(address)


#13_2_3
print('Ответ 13_2_3:', end = " ")
address = ip_network('84.77.95.123/255.255.224.0', 0)
print(address) # байт = октет


#13_3
print('Ответ 13_3:', end = " ")
host = "162.198.0.157"
address = ip_network(f'{host}/255.255.255.224', 0)
k = 1
for i in address.hosts():
	if str(i) == host:
		print(k)
		break
	k += 1
	
	
#13_3_1
print('Ответ 13_3_1:', end = " ")
host = "10.18.134.220"
address = ip_network(f'{host}/255.255.255.192', 0)
k = 1
for i in address.hosts():
	if str(i) == host:
		print(k)
		break
	k += 1
	
	
#13_3_2
print('Ответ 13_3_2:', end = " ")
host = "112.154.133.208"
address = ip_network(f'{host}/255.255.248.0', 0)
k = 1
for i in address.hosts():
	if str(i) == host:
		print(k)
		break
	k += 1


#13_3_3
print('Ответ 13_3_3:', end = " ")
host = "206.158.124.67"
address = ip_network(f'{host}/255.255.224.0', 0)
k = 1
for i in address.hosts():
	if str(i) == host:
		print(k)
		break
	k += 1	
	
	
#13_4
print('Ответ 13_4:', end = " ")
address = ip_network('0.0.0.0/255.255.254.0')
print(len(list(address.hosts())))


#13_4_1
print('Ответ 13_4_1:', end = " ")
address = ip_network('0.0.0.0/255.255.255.192')
print(len(list(address.hosts())))


#13_4_2
print('Ответ 13_4_2:', end = " ")
address = ip_network('0.0.0.0/255.255.248.0')
print(len(list(address.hosts())))


#13_4_3
print('Ответ 13_4_3:', end = " ")
address = ip_network('0.0.0.0/255.255.255.128')
print(len(list(address.hosts())))


#13_4_4
print('Ответ 13_4_4:', end = " ")
address = ip_network('0.0.0.0/255.255.255.224')
print(len(list(address.hosts())))


#13_5
print('Ответ 13_5:', end = " ")
for mask in range(33):
	address = ip_network(f'224.128.112.142/{mask}', 0)
	# network_address удаляет маску из IPv4Address
	if str(address.network_address) == "224.128.64.0": 
		# netmask выводит только маску
		print(address.netmask) 


#13_5_1
print('Ответ 13_5_1:', end = " ")
for mask in range(33):
	address = ip_network(f'224.128.114.142/{mask}', 0)
	# network_address удаляет маску из IPv4Address
	if str(address.network_address) == "224.128.64.0": 
		# netmask выводит только маску
		print(address.netmask) 


#13_5_2
print('Ответ 13_5_2:', end = " ")
for mask in range(33):
	address = ip_network(f'224.128.114.142/{mask}', 0)
	# network_address удаляет маску из IPv4Address
	if str(address.network_address) == "224.128.96.0": 
		# netmask выводит только маску
		print(address.netmask) 


#13_5_3
print('Ответ 13_5_3:', end = " ")
for mask in range(33):
	address = ip_network(f'117.191.88.37/{mask}', 0)
	# network_address удаляет маску из IPv4Address
	if str(address.network_address) == "117.191.80.0": 
		# netmask выводит только маску
		print(address.netmask) 


#13_5_4
print('Ответ 13_5_4:')
for mask in range(33):
	address = ip_network(f'154.201.208.17/{mask}', 0)
	# network_address удаляет маску из IPv4Address
	if str(address.network_address) == "154.201.192.0": 
		# netmask выводит только маску
		print(address.netmask) 
		
		
#13_6
print('Ответ 13_6:')
for mask in range(33):
	address = ip_network(f'98.162.71.94/{mask}', 0)
	if str(address.network_address) == "98.162.71.64":
		print(address, len(list(address.hosts()))+2) 
		# +2 так как hosts() не содержит в себе первый и последний адрес
		

#13_6_1
print('Ответ 13_6_1:')
for mask in range(33):
	address = ip_network(f'98.162.71.94/{mask}', 0)
	if str(address.network_address) == "98.162.71.64":
		print(address, len(list(address.hosts()))+2) 
		# +2 так как hosts() не содержит в себе первый и последний адрес
		# Можно использовать num_addresses и тогда не нужно будет добавлять 2
		

#13_7
print('Ответ 13_7:', end = " ")
address = ip_network('192.168.32.160/255.255.255.240', 0)
k = 0
for ip in address:
	if bin(int(ip))[2:].zfill(32).count('1')%2 == 0:
		k += 1
print(k)


#13_7_1
print('Ответ 13_7_1:')
for mask in range(32):
	address = ip_network(f'122.21.49.91/{mask}', 0)
	if str(address.network_address) == "122.21.48.0":
		print(address)
	

#13_7_2
print('Ответ 13_7_2:', end = ' ')
address = ip_network('10.48.96.0/255.255.240.0', 0)
k = 0
for ip in address:
	if bin(int(ip))[2:].zfill(32).count('1') > 16:
		k += 1
print(k)
		
		
#13_8
print('Ответ 13_8:')
for mask in range(32):
	address1 = ip_network(f'165.112.200.70/{mask}', 0)
	address2 = ip_network(f'165.112.175.80/{mask}', 0)
	if address1 == address2:
		print(mask)


#13_8_1
print('Ответ 13_8_1:')
for mask in range(32):
	address1 = ip_network(f'10.96.180.231/{mask}', 0)
	address2 = ip_network(f'10.96.140.118/{mask}', 0)
	if address1 != address2:
		print(32 - mask)







