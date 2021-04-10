'''
Assignment No: 4
To accept students five courses marks and compute his/her result. 
Student is passing if he/she scores marks equal to and above 40 in each course. 
If student scores aggregate greater than 75%, then the grade is distinction. 
If aggregate is 60>= and <75 then the grade if first division. 
If aggregate is 50>= and <60, then the grade is second division. 
If aggregate is 40>= and <50, then the grade is third division.
'''

n = int(input("number of subjects: "))
sum1 = 0

for i in range(n):
    k = int(input("subject %d: " %(i+1)))
    if(k < 40):
        print("fail")
        break
    sum1 = sum1 + k

agg = (sum1/n)
print("aggregate = ",agg)

if(agg >= 75):
    print("Distinction")
elif(agg >= 60 and agg < 75):
    print("First Division")
elif(agg >= 50 and agg < 60):
    print("Second Division")
else:
    print("Third Division")

