'''
Assignment No:3
To accept N numbers from user. Compute and display maximum in list, minimum in list, 
sum and average of numbers using built-in function.
'''

n = int(input("Enter number of inputs: "))
numlst = []
for i in range(n):
    l = int(input("number %d : " %(i + 1)))
    numlst.append(l)

max_no = max(numlst)
min_no = min(numlst)

summation = sum(numlst)
average = summation/n

print("Maximum number = ", max_no)
print("Minimum number = ", min_no)
print("Summation of numbers = ", summation)
print("Average of numbers = ", average)
