s = input("IP address: ")
for i in s:
    s = s.replace('.', ',')

print("Defanged IP:",s)
