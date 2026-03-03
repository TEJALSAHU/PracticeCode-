#no.range tester
# write a python prgm to test whether a no. is within 100 of 1000 or 2000
num = int(input("Enter a number: "))
if (abs(1000 - num) <= 100) or (abs(2000 - num) <= 100):
    print("The number is within 100 of 1000 or 2000.")
   
