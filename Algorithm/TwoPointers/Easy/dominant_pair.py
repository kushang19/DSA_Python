# Find the number of Dominant Pairs

# Given an even-sized array arr[] of length n. A dominant pair (i, j) is defined as:

# i belongs to the first half of the array, (0 <= i < n/2)
# j belongs to the second half of the array, (n/2 <= j < n)
# The value at index i is at least five times the value at index j, (arr[i] >= 5 * arr[j])
# The task is to find the count of total number of dominant pairs in the array


# Examples:

# Input: arr[] = [10, 2, 2, 1]
# Output: 2
# Explanation: First half: [10, 2], Second half: [2, 1]. So valid pairs are: 

# {0, 2}: 10 >= 5 × 2 
# {0, 3}: 10 >= 5 × 1 
# So, total dominant pairs = 2.

# Input: arr[] = [10, 8, 2, 1, 1, 2]
# Output: 5
# Explanation: First half: [10, 8, 2], Second half: [1, 1, 2]. So valid pairs are: 

# {0, 3}: 10 >= 5 × 1
# {0, 4}: 10 >= 5 × 1 
# {0, 5}: 10 >= 5 × 2
# {1, 3}: 8 >= 5 × 1 
# {1, 4}: 8 >= 5 × 1 
# So, total dominant pairs = 5.


# ================================ Two Pointer Method =================================
# Using Sorting + Two Pointers - O(n*log(n)) Time and O(1) Space

arr = [10, 8, 2, 1, 1, 2]
# arr = [10, 2, 2, 1]

def dominant_pair(arr):
    n = len(arr)
    mid = n//2
    left = arr[:mid]
    right = arr[mid:]

    left.sort()
    right.sort()

    print(left, right)
    j = 0
    count = 0

    for i in range(len(left)):
        while j < len(right) and left[i] >= 5*right[j]:
            j += 1
        count += j
    
    print("count:",count)
dominant_pair(arr)






# [Brute-Force Approach] Using 2 Nested Loops - O(n²) Time and O(1) Space

# arr = [10, 8, 2, 1, 1, 2]
# # arr = [10, 2, 2, 1]

# def dominant_pair(arr):
#     n = len(arr)
#     count = 0

#     for i in range(0,n//2):
#         for j in range(n//2, n):
#             if arr[i] >= 5*arr[j]:
#                 count += 1
    
#     print("count: ", count)

# dominant_pair(arr)