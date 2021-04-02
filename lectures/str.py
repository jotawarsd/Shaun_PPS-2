str1 = "welcome to the world of python"
print(str1[:])
print(str1[1:5])
print(str1[1:20:2])#slicing operation-[start:end:increment]

s1 = "good Morning"
print(s1.capitalize())
print(s1.upper())
print(s1.lower())
print(s1.swapcase())
print(s1.isupper())
print(s1.islower())
print(list(enumerate(s1)))
print(len(s1))
print(min(s1))
print(max(s1))
print(s1.replace("o", "w"))

s2 = "abc69"
s3 = "fdjh"
s4 = "69420"
print(s2.isalnum())#checks if string is alphanumeric
print(s3.isalpha())#only alphabet
print(s4.isdigit())#only numbers

s5 = "hellohello hellohello"
m1 = "ll"
print(s5.count(m1,0,len(s5)))#counts number of times a given string appears in the string2 #count(string_to_find,start_index,end_index)
print(s5.startswith("he",0,len(s5)))#boolean for start of string
print(s5.endswith("loo",0,len(s5)))     
print(s5.find("he",6,len(s5)))#gives index of string

s6 = "hello"
print(s6.ljust(10,"*"))#ljust(no_ofindex, characters to add) #starts from left and adds given character in spaces after string
print(s6.rjust(10,"*"))#starts from right
print(s6.center(11,"*"))#centres string inside the no. of index. adds character in blank spaces

s7 = "1234"
print(s7.zfill(6))#zfill(width of output string)#adds 0 to remaining spaces to the left

s8 = "hello hello hello"
#      |2          |1     rfind will count from 1 to 2 if input is he
#      |           |      rindex will count from end to he
print(s8.rfind("he",0,len(s1)))
print(s8.rindex("he",0,len(s1)))

s9 = "welcome to python"
x = s9.split()
print(x)
print(" ".join(x))
s10 = "shaun123"#string should contain atleast 1 alphabetical character to give true in isidentifier funct
print(s3.isidentifier())#checks for validity of identifier. here s3 is a valid string

import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)

s11 = "    hello"
print(s11.lstrip())
print(s11.rstrip())
print(s11.strip())

l = "h" 
m = "i" 
print(l + m)
