#!/usr/bin/python3


template = [    'define host {',
		'use dedicated-server',
		'host_name',
		'alias',
		'address',
		'hostgroups dedicated-servers',
	        'contacts internal',
        	'} \n']

ip = 'D0028 100.100.100.167 D0067 200.200.200.95 D0139 300.300.300.222'

ip2 = list()
ip2 = ip.split(' ')
for a in ip2:
    a = '\'' + a + '\''
servers = dict(zip(ip2[::2],ip2[1::2]))


for name, ip in servers.items():
	print('#Play ' + name + ' ' + ip)
	for line in template:
		if line.endswith('host_name'):
			print('{} {}'.format(line, name))
		elif line.endswith('alias'):
			print('{} {}'.format(line,'Play ' + name))
		elif line.endswith('address'):
			print('{} {}'.format(line,ip))
		else:
			print(line)



