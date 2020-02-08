"""
Program: program that
takes as inputs the hourly wage, total regular hours, and total overtime hours
and
displays an employee’s total weekly pay
Author: Kaleo Kelikani



Inputs:

Hourly wage
total regular hours
total overtime hours

output print total weekly pay

weekly pay is hourly wage * regular hours + overtime hours * (1.5 * hourly wage)

compute

input require
hourly wage
# of regular hours
# of overtime hours


"""

hourly=float(input("Enter Hourly Wage $  " ))
reghours=float(input("Enter Number hours reg work week  "))
overtime=float(input("Enter number of hours worked over 40 hours per week  "))
overtimewage=(overtime * (1.5 * hourly))
regwage=(hourly * reghours)
total=(regwage + overtimewage)
print("Regular wage for the week "'${:,.2f}'.format (regwage))
print("Overtime wage for the week "'${:,.2f}'.format (overtimewage))
print("Total compensation for the week is:  "'${:,.2f}'.format(total))

