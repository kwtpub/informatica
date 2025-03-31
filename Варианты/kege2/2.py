a = '8' * 83
while '111' in a or '88888' in a:
	if '111' in a:
		a = a.replace('111', '8', 1)
	else:
		a = a.replace('88888', '8',1)

print(a)