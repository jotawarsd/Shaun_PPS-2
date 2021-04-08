n = int(input("number of subjects: "))
sum1 = 0

for i in range(n):
    k = int(input("marks: "))
    sum1 = sum1 + k

agg = (sum1/n)
print("aggregate = ",agg)

if(agg >= 75):
    print("Distinction")
elif(agg >= 60 and agg < 75):
    print("First Division")
elif(agg >= 50 and agg < 60):
    print("Second Division")
elif(agg >= 40 and agg < 50):
    print("Third Division")
else:
    print("fail")
