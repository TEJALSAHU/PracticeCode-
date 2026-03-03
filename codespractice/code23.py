#Write a Python program to test whether a passed letter is a vowel or not
def is_vowel(char):
    vowels = 'aeiouAEIOU' #define a string containing all the vowels (both lowercase and uppercase)
    if char in vowels: #check if the input character 'char' is present in the 'vowels' string
        return True #if it is, return True indicating that it is a vowel
    else:
        return False #if it is not, return False indicating that it is not a vowel
    
#test the function with different input characters
print(is_vowel('a'))  # Output: True
print(is_vowel('E'))  # Output: True
print(is_vowel('z'))  # Output: False