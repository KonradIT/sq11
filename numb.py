## Proof of concept -- Run this on a supercomputer -- it *will* crash
## Flags:
debug=True
print_for_x=True

import sys

i = 1
if len(sys.argv) > 1:
	i = int(sys.argv[1])
while str(i**2)[-2:] != '11':
	if len(sys.argv) > 1:
		if i == int(sys.argv[2])+1:
			break
	x = str(i**2)
	if debug == True:
		print("i int: " + str(i))
	if print_for_x == True:    
		print("i^2 int: " + str(x))
	i += 1
if str(i**2)[-2:] == '11':
	print ("magical number; " + str(i) + ' -- ' + str(i**2))
