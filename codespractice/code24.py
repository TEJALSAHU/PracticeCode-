#Write a Python program that checks whether a specified value is contained within a group of values
def is_group_member(group_data, n):
    if n in group_data: #check if the specified value 'n' is present in the group of values 'group_data'
       return True #if it is, return True indicating that it is a member of the group
    else:
        return False #if it is not, return False indicating that it is not a member of the group
#test the function with different inputs
print(is_group_member([1, 2, 3, 4], 3))
print(is_group_member('Python', 'y'))
print(is_group_member((1, 2, 3), 4))