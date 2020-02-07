"""
Program: takes as input a number of kilometers and prints the
corresponding
number of nautical miles from km.

Author: Kaleo Kelikani

Data gathered
A kilometer represents 1/10,000 of the
distance between the North Pole and
the equator.

There are 90 degrees, containing 60 minutes
of arc each, between the North
Pole and the equator.

A nautical mile is 1 minute of an arc.

#

Compute
Algebraic Steps / Dimensional Analysis Formula
10 km	*	100000 cm
1 km	*	1 in
2.54 cm	*	1 nmi
72913.3858 in	=	5.399568035 nmi

Direct Conversion Formula

The symbol for nautical mile is M or NM or nmi.
There are 0.5399568 nautical miles in a kilometer
nautical miles = km ÷ 1.852

"""
kilomile = int(input("Enter the distance in Kilometer   " ))
kilomile

nauticalmile=round(kilomile/1.852 , 4)

print(kilomile ,"kilometers is equal to  :" , nauticalmile , "nm")



