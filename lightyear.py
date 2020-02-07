"""
Program: calculates and displays the value of a
light-year.

Author: Kaleo Kelikani

1.Compute # of seconds in one year and multipy by 3 * 10**8

3.Computations are:

Light travels at 3 *108 meters per second
#
"""
# Constrictions are
#Light travels at 3 * 10 **8 meters per second
# Compute
minutes=int(60)
minutes
hours=int(24)
hours
days=int(365)
days
year=(minutes * hours * days )
year
secondsy=(year * 60)
secondsy
lightyearv=((secondsy * 3) * (10 ** 8))
lightyearv
print("This is the value of a lightyear", lightyearv, "km")


