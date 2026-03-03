#get a string which is n (non-negative integer) copies of a given string
def string_times(text,n):
    result = "" #initialize an empty string to store the result
    for i in range(n): #iterate n times
        result += text #append the input string 'text' to the result in each iteration
    return result #return the final concatenated string
#test the function with different inputs
print(string_times("Hi", 2))  # Output: "HiHi"  
print(string_times("Hi", 3))  # Output: "HiHiHi"