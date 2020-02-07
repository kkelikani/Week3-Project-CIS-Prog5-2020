"""
Program: That accepts mass in kg to come up with objects momentum and also the
kinetic energy of the object

Author: Kaleo Kelikani

1.Compute mass * velocity
  also compute KE fo the object

2. Input = mass kg

3.Computations are:

# Formulas to obtain objects momentum is mass x velocity
  KE = (1/2)mv2

"""
# Request input for the radius of the sphere
mass=int(input("Enter the size of the mass is kg of object:  "))
mass
velocity=int(input("Enter the velocity in meters per second:  "))
momentum=(mass * velocity)
kineticenergy=((1/2 * mass) * (velocity **2))
print("The momentum of the object is :  ", momentum,"kg m/s")
print("The KE of the object is :  " + "{:.0f}".format(kineticenergy))
