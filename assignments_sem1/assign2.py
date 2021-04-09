'''
Assignment No: 2
To accept an object mass in kilograms and velocity in meters per second and display its momentum. 
Momentum is calculated as e=mc2 where m is the mass of the object and c is its velocity. 
'''

mass = float(input("mass:"))    #input of mass
velocity = float(input("velocity:"))    #input of velocity
momentum = mass * (velocity**2)    #calculating momentum
print("momentum =",momentum)    #printing momentum
