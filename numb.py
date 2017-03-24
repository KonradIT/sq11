## Proof of concept -- Run this on a supercomputer -- it *will* crash
## Flags:
debug=True
print_for_x=True
i = 1
while str(i**2)[-2:] != '11':
	x = str(i**2)[-2:]
	if debug == True:
		print("i int: " + str(i))
	if print_for_x == True:    
		print("x int: " + str(x))
	i += 1
print ("magical number; " + str(i) + ' -- ' + str(i**2))
