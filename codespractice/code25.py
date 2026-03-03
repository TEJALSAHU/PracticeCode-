#Write a Python program to create a histogram from a given list of integers.
def histogram(items):
    for n in items: #iterate through each integer 'n' in the input list 'items'
        output = '' #initialize an empty string to build the histogram line for the current integer
        times = n #store the value of 'n' in a variable 'times' to determine how many asterisks to print
        while times > 0: #continue looping until 'times' is greater than 0
            output += '*' #append an asterisk to the 'output' string for each iteration
            times -= 1 #decrement 'times' by 1 in each iteration
        print(output) #print the histogram line for the current integer

#test the function with a sample list of integers
histogram([4, 9, 7])