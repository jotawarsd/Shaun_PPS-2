'''
Assignment No: 8 
To copy contents of one file to other. While copying a) all full stops are to be 
replaced with commas b) lower case are to be replaced with upper case c) upper case 
are to be replaced with lower case. 
'''

fin = open("input.txt",'r')		# file open in read mode
fout = open("output.txt",'w')		# file created 

for line in fin:
   line = line.swapcase() 		#Replace lower case with upper and upper with lower
   line = line.replace(".",",")		#Replace full stops with comma
   fout.write(line)
