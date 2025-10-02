# Rearrange array such that even positioned are greater than odd (1-based indexing)

# Given an array arr[], sort the array according to the following relations:  

# arr[i] >= arr[i - 1], if i is even, ∀ 1 <= i < n
# arr[i] <= arr[i - 1], if i is odd, ∀ 1 <= i < n
# Find the resultant array.[consider 1-based indexing]

# Examples:  

# Input: arr[] = [1, 2, 2, 1]
# Output: [1 2 1 2]
#  Explanation:
# For i = 2, arr[i] >= arr[i-1]. So, 2 >= 1.
# For i = 3, arr[i] <= arr[i-1]. So, 1 <= 2.
# For i = 4, arr[i] >= arr[i-1]. So, 2 >= 1.

# Input: arr[] = [1, 3, 2]
# Output: [1 3 2]

def even_greater(a):
    a.sort()
    print(a)
    n = len(a)
    res = [0] * n
    prt1,prt2 = 0, n-1

    for i in range(n):
        if(i+1) %2 == 0:
            res[i] = a[prt2]
            prt2 -= 1
        else:
            res[i] = a[prt1]
            prt1 += 1 

    return res

arr = [2, 4, 3, 5, 6]

print(even_greater(arr))