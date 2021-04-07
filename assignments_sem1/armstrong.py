N = input("Enter number: ")
s = 0
for i in range(len(N)):
    s = s + ((int(N[i]))**3)
print(s)

if(s == int(N)):
    print("The given number is an Armstrong number")
else:
    print("The given number is not an Armstrong number")

