#Python: How to check if a number is odd or even?
#take input from the user
num = int(input("Enter a number: "))
#check if the number is even or odd
mod = num % 2
if mod > 0:
    print("The number is odd.")
else:
    print("The number is even.")