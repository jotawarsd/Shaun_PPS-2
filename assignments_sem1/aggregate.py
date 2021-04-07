n = int(input("number of subjects: "))
sum1 = 0

for i in range(n):
    k = int(input("marks: "))
    sum1 = sum1 + k

agg = (sum1/n)
print("aggregate = ",agg)

if(agg >= 75):
    print("class: distinction")
elif(agg >= 60 and agg < 75):
    print("class: first class")
elif(agg >= 50 and agg < 60):
    print("class: second class")
elif(agg >= 40 and agg < 50):
    print("class: third class")
else:
    print("fail")