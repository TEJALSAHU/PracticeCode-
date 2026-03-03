#WAP to calculate the number of days between two dates

#cal no. of days b/t two dates
from datetime import date #import the date class from the datetime module
f_date = date(2026,2,16)#define start date
l_date = date(2026,4,18)#define end date
delta = l_date - f_date #cal the d/f
print(delta.days)
