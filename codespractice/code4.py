#WAP to display the current date and time


#import the 'datetime' module to work with date and time
import datetime
#get the current date and time
now = datetime.datetime.now()
#display the msg indicating what is being printed
print("Current date and time :")
#print the current date and time in specific format 
print(now.strftime("%Y-%m-%d %H:%M:%S"))