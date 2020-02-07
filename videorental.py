"""
Program: Calculate the total charge for video rentals per customer
Author: Kaleo Kelikani
Calculate total rental charges for video rental customer 

Initialize Constraints:

Video rental are different for New and Oldies

New rental per night cost $3.00 per night
Oldie rental per night cost $2.00 per night

Request input:
# of New rental
# of Oldie rental

Output total cost of

(number of new rentals * $3.00) + (number of oldie rental * $2.00)

"""

newrental= int(input("Enter the # of New Rentals:  "))
newrental
oldierental= int(input("Enter the # of Oldie Rentals:  "))
oldierental
newrentalcost=round(newrental * 3 , 2)
newrentalcost
oldierentalcost=round(oldierental * 2, 2)
oldierentalcost
print("Total Cost of Rental  $", newrentalcost + oldierentalcost)

