'''

'''

num1 = input("number : ")   #get input from user

def reverse(s1):
    n = len(s1) - 1   #establish index of last digit
    for i in range(n,-1,-1):    #printing the number in reverse
        print(s1[i], end='')

reverse(num1)
