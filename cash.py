n = float(input("amount of cash: "))
deno = [1, 5, 10, 20, 50, 100, 200, 500, 2000]
x = 0
for i in range(8,0,-1):
    while (n < deno[i] and n >= deno[i-1]):
        n = n - deno[i]
        x = x + 1
print(x)

