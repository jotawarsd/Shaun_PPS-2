'''

Assignment no. 7
To write a python program that accepts a string from user and performs the following string operations- 
i. Calculate length of string 
ii. String reversal 
iii. Equality check of two strings 
iv. Palindrome check
v. Substring check

'''

string = input("Enter string : ")   #obtain an input as a string from the user

print("1.Length \n2.Reversal \n3.Equality of 2 strings \n4.Palindrome check \n5.Substring check") 
choice = int(input("Enter choice number: "))    #enlist choices of functions and allow the user to choose from them

#define equality function
def equality(a):
    l = input("Enter string to compare: ")    #obtain second string for comparison
    if(l == a):                               #check equality
        print("Strings are equal")
    else:
        print("Strings are not equal")

#define palindrome function
def palindrome(b):
    #check whether the given string is a palindrome
    if(b[::-1] == b):
        print("%s is a palindrome" %(b))
    else:
        print("%s is not a palindrome" %(b))

#define substring function
def substring(c):
    m = input("Enter substring to check: ")    #obtain second string for comparison
    if m in c:                                 #check whether second string is the subset of the given string
        print("%s is a substring of %s" %(m,c))
    else:
        print("%s is not a substring of %s" %(m,c))

if(choice == 1):
    print("Length of string = ", len(string))       #print length of string
elif(choice == 2):
    print("reverse of string : ", string[::-1])     #print reverse of string  
elif(choice == 3):
    equality(string)                                #check equality
elif(choice == 4):
    palindrome(string)                              #check palindrome
elif(choice == 5):
    substring(string)                               #check substring
else:
    pass

