
#exercise 1
print("Twinkle, twinkle, little star,\nHow I wonder what you are! ,\n\t\t Up above the world so high,\n\t \tLike a diamond in the sky, \n\t Twinkle, twinkle, little star, \n\t How I wonder what you are!")

#exercise 2
import sys
print("Python version")
print(sys.version)

#exercise 3
import sys
print("version info")
print(sys.version_info)

#exercise 4
import platform
print(platform.python_version())

#exercise 5
from math import pi #import pi constant  from the math module to cal. area of the circle
r= float(input("Input the radius of the circle:")) #take input from theh user
#cal. the area of the circle
area = pi*r**2
#display trhe result ,including the radius and calculated area
print("the area of the circle with radius "+ str(r) +  "  is:  " + str(area))

#exercise 6
#import the 'datetime' module to work with date and time
import datetime
#get the current date and time
now = datetime.datetime.now()
#display the msg indicating what is being printed
print("Current date and time :")
#print the current date and time in specific format 
print(now.strftime("%Y-%m-%d %H:%M:%S"))

#exercise 7
#reverse name
fname = input("Input your first name :")
lname = input("Input your last name :")
print("Hello  " + lname + " " + fname)

#exercise 8
#list tuple generator
values = input("Input some comma-separated numbers: ")
list = values.split(",")
tuple = tuple(list)
print('List: ', list)
print('Tuple :', tuple)

#exercise 9
# file extractor
filename = input("Input the Filename:")
f_extns = filename.split(".")
print ("The extension of the file is :" + repr(f_extns[-1]))

#exercise 10
#first and last color
color = ["red","green","white","black"]
print( "%s %s" % (color[0],color[-1]))         

#exercise 11
exam_st_date= (11,12,2024)
print ("The examination will start from : %i %i %i" % exam_st_date)

#exercise 12
#no. expansion calculator
a = int(input("Input an integer: "))

# Create new integers 'n1', 'n2', and 'n3' by concatenating 'a' with itself one, two, and three times, respectively
n1 = int("%s" % a)          # Convert 'a' to an integer
n2 = int("%s%s" % (a, a))   # Concatenate 'a' with itself and convert to an integer
n3 = int("%s%s%s" % (a, a, a))  # Concatenate 'a' with itself twice and convert to an integer

# Calculate the sum of 'n1', 'n2', and 'n3' and print the result
print(n1 + n2 + n3)

#exercise 13
#print the docstring of the built-in 'abs()' funct,
print(abs.__doc__)
#print docstring of len func
print(len.__doc__)
#sorted
print(sorted.__doc__)
#sum()
print(sum.__doc__)
#map()
print(map.__doc__)
#filter()
print(filter.__doc__)

#exercise 14
#monthly calender display
import calendar
#take user input
y= int(input("Input the year: "))
m= int (input("Input the month:"))
print(calendar.month(y,m))

#exercise 15
#use triplr double-quotes to create a multi-line string
print(""" a string that you "don't" have to escape
      This 
      is a ....... multi-line
      heredoc string --------> example
      """)

#exercise 16
#cal no. of days b/t two dates
from datetime import date #import the date class from the datetime module
f_date = date(2026,2,16)#define start date
l_date = date(2026,4,18)#define end date
delta = l_date - f_date #cal the d/f
print(delta.days)

#exercise 17
#print sphere vol calendar
pi = 3.141592653589793#define val of pi
r= 6.0 # define radius of sphere
v= 4.0/3.0 *pi * r**3 #cal. the vol of the sphere using the formula V = 4/3 * pi * r^3
print ("The vol of the sphere is :", v)

#exercise 18
#Cal the sum of three given no.s, if the val are equal then return thrice of their sum
def sum_thrice(x,y,z):
    sum = x+y+z#cal the sum of x,y,z
    if x==y==z:
        sum = sum*3
        return sum #if they are equal, triple the sum
print(sum_thrice(1,2,3))
print (sum_thrice(3,3,3))


#exercise 19
#prefix "is" sting modifier
def new_string(text):#define a fun name "new_sting"that take str para called "text"
    if len(text) >= 2 and text[:2] == "Is":
        return text
    else:
        return "Is" + text
    print(new_string("Array"))
    print(new_string("IsEmpty"))

#exercise 20
#     