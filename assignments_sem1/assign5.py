'''
Assignment No: 5
To check whether input number is Armstrong number or not. 
An Armstrong number is an integer with three digits such that the sum of the cubes of its digits is equal to the number itself. 
Ex. 371.
'''

N = input("Enter number: ")
s = 0
for i in range(len(N)):
    s += ((int(N[i]))**3)

if(s == int(N)):
    print("The given number is an Armstrong number")
else:
    print("The given number is not an Armstrong number")

