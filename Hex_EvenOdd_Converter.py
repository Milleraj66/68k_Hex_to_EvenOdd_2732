#!/usr/bin/python
# Author:   	Arthur J. Miller using simpson's approx. algorithm form wikipedia
# Date:     	08-09-2016
# Purpose:  	convert hex input for one ROM to hex input for even odd 2732 EPROM
#		Input:	text file with unformatted HEX data
#		Output:	text file with Even/Odd Bytes					

import os # remove


# Function to calculate Normal cumulative distribution function 
def main():
	fname = "foo.txt" 			# Input Hex file name
	OutputEven = "Even.hex"		# Output Even Bytes filename
	OutputOdd = "Odd.hex"		# Output Odd Bytes Filename
	counter = 0 				# even odd counter
	Even = []					# List stores Even Bytes
	Odd = []					# List stores Odd Bytes
	
	# Open Hex file
	# Read Line of Hex data and convert to Even, Odd Bytes
	with open(fname, "rb+") as f:
		for line in f:
			for Byte in line.split():
				if(counter % 2 == 0):
					Even.append(Byte)
				else:
					Odd.append(Byte)
				counter += 1
	# Close inputed hex file
	f.close()
	
	# Delete Even.hex && Odd.hex if exists
	try:
		os.remove(OutputEven)
	except OSError:
		pass
	try:
		os.remove(OutputOdd)
	except OSError:
		pass			
	
	# Convert lists to strings
	EvenStr = ''.join(Even)
	OddStr = ''.join(Odd)
    
    # Write Even.hex && Odd.hex
	with open(OutputEven, 'w+') as f:
		f.write(EvenStr)
	f.close()
	with open(OutputOdd, 'w+') as f:
		f.write(OddStr)
	f.close()
    
  

# Driver function
# User can modify precision and total computations with stop,step values
if __name__ == '__main__':
    main()
