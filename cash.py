n = float(input("amount of cash: "))
deno = [0, 1, 5, 10, 20, 50, 100, 200, 500, 2000]
x = 0

for i in range(9,0,-1):
    if (n >= deno[i]):
        while (n >= deno[i]):
            n = n - deno[i]
            x += 1
            print(deno[i])
    else:
        continue

print("minumum number of denominations =", x)
