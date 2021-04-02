s = input("IP address:")
l1 = []
for i in range(len(s)):
    l1.append(s[i])
    if(s[i] == '.'):
        l1.remove(s[i])
        l1.insert(i,'[.]')
    print(l1[i],end='')
