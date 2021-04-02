key = int(input("key: "))
s = str(input("text: "))
x = 0
for i in s:
    x = ord(i) + key
    print(chr(x),end = '')
