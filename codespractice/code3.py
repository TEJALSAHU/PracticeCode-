#WAP to calculate the area of a circle by taking the radius as input from the user

from math import pi #import pi constant  from the math module to cal. area of the circle
r= float(input("Input the radius of the circle:")) #take input from theh user
#cal. the area of the circle
area = pi*r**2
#display trhe result ,including the radius and calculated area
print("the area of the circle with radius "+ str(r) +  "  is:  " + str(area))