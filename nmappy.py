#!/usr/bin/env python
import nmap
import os

# take the range of ports to 
# be scanned 
begin = 22
end = 80

# assign the target ip to be scanned to 
# a variable 
target = '65.61.137.117'

# instantiate a PortScanner object 
scanner = nmap.PortScanner() 

for i in range(begin,end+1): 

	# scan the target port 
	res = scanner.scan(target,str(i)) 

	# the result is a dictionary containing 
	# several information we only need to 
	# check if the port is opened or closed 
	# so we will access only that information 
	# in the dictionary 
	res = res['scan'][target]['tcp'][i]['state'] 

	print(f'port {i} is {res}.') 
