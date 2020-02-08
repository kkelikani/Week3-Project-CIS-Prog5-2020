"""
Program: Find the diameter, circumfrence, surface area, and volume of sphere
with radius given

Author: Kaleo Kelikani

1.Compute the a Sphere's diameter, circumfrence, surface area, and volume

2. Input = radius the of the sphere

3.Computations are:

# Formulas for diameter:
# d=2r
#circumfrence is 2*3.14*r
#surface of a sphere is A=4*3.14*r squared
#volume of a sphere is V=4/3 *3.14*r3

"""
# Request input for the radius of the sphere
radius= float(input("Enter the size of the radius of the sphere:  "))
radius
diameter=(2 * radius)
diameter
circumfrence=round(2 * 3.14 * radius ,4)
circumfrence
volume=((1.3333 * 3.14) * (radius **3))
volume
areaofsphere=((4 * 3.14) * (radius **2))
areaofsphere
print("Circumfrence of sphere is:  ", circumfrence,"m")
print("Diameter of sphere is: ", diameter,"m")
print("Volume of sphere is: ", volume,"m3")
print("Area of sphere is: ", areaofsphere,"m2")



