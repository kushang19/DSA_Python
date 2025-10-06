# Mean of array using recursion
# Last Updated : 22 Apr, 2025
# Given an array of numbers, you are required to calculate the mean (average) using recursion.

# Note: The mean of an array is the sum of its elements divided by the number of elements in the array.

# Examples: 

# Input: 1 2 3 4 5
# Output: 3
# Explanation: The sum of elements (15) divided by the number of elements (5) gives the mean: 3

# Input: 1 2 3
# Output: 2
# Explanation: The sum of elements (6) divided by the number of elements (3) gives the mean: 2


arr = [1, 2, 3, 4, 5]
# arr = [1, 2, 3]
sum = 0
n = len(arr)

def mean_of_array(a,s,n):
    l = len(a)
    if n < 0:
        return s//l
    else:
        s += a[n]
        return mean_of_array(a,s,n-1) 


print(mean_of_array(arr,sum,n-1))