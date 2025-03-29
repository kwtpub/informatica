from ipaddress import * 

address = ip_network('112.154.133.208/21',0)
k = 1
for i in address.hosts():
	if str(i) == '112.154.133.208':
		print(k)
		break
	k += 1 #1488
