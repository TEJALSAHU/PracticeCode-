#WAP in Python: n (non-negative integer) copies of the first 2 characters of a given string
def susbstring_copy(text,n):
    flen = 2 #define the length of the substring to be copied
    if flen > len(text): #check if the length of the substring is greater than the length of the input string
        flen = len(text) #if it is, set the length of the substring to the length of the input string
    substr = text[:flen] #get the substring to be copied
    result = "" #initialize an empty string to store the result
    for i in range(n): #iterate n times
        result += substr #append the substring to the result in each iteration
    return result #return the final concatenated string
#test the function with different inputs        
print(susbstring_copy("Python", 3))  # Output: "PyPyPy"
print(susbstring_copy("Hi", 5))      # Output: "HiHiHi