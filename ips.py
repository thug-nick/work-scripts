#!/usr/bin/python3

ip = 'D0028 100.100.100.167 D0067 200.200.200.95 D0139 300.300.300.222'

ip2 = list()
ip2 = ip.split(' ')
#print(ip2)
for a in ip2:
    a = '\'' + a + '\''
result = dict(zip(ip2[::2],ip2[1::2]))

print(result)
