""" # Demonstrated Python Program
# to read file character by character
file = open('gfg.txt', 'r')

while 1:
	
	# read by character
	char = file.read(1)		 
	if not char: 
		break
		
	print(char)

file.close()
 """
 
 # Python code to demonstrate 
# Read character by character
with open('gfg.txt') as f:
	
	while True:
		
		# Read from file 
		c = f.read(5)
		if not c:
			break

		# print the character
		print(c)
