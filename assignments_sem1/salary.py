'''

Assignment No: 1
To calculate salary of an employee given his basic pay (take as input from user). 
Calculate gross salary of employee. Let HRA be 10 % of basic pay and TA be 5% of basic pay. 
Let employee pay professional tax as 2% of total salary. 
Calculate net salary payable after deductions.

'''

n = int(input("enter base salary: "))   #take input of base salary of an employee from the user

HRA = 0.10*n    #calculate HRA
TAB = 0.05*n    #calculate TAB
total = n + HRA + TAB   #calculate total salary

PT = 0.02*total     #calculate Proffesional Tax
net = total - PT    #calculate net salary payable to the employee

print(net)    #print net salary
