#Python: Count the number of occurrences in a list
def list_count_4(nums):
    count=0 #initialize a counter variable to keep track of occurrences
    for num in nums: #iterate through each number in the input list 'nums'
        if num == 4: #check if the current number is equal to 4
            count += 1 #if it is, increment the counter by 1
    return count
#test the function with different input lists
print(list_count_4([1, 2, 3, 4, 5, 4]))  # Output: 2
print(list_count_4([4, 4, 4, 4]))        # Output: 4
print(list_count_4([1, 2, 3, 5]))        # Output: 0