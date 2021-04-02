n = int(input("enter base salary: "))
HRA = 0.10*n
TAB = 0.05*n
tax = 0.02*n
net = n + HRA + TAB - tax
print(net)
