# Given a sorted array arr[] of size n, the goal is to rearrange the array so that all distinct elements appear at the beginning in sorted order. Additionally, return the length of this distinct sorted subarray.

# Note: The elements after the distinct ones can be in any order and hold any value, as they don't affect the result.

# Examples: 

# Input: arr[] = [2, 2, 2, 2, 2]
# Output: [2]
# Explanation: All the elements are 2, So only keep one instance of 2.

# Input: arr[] = [1, 2, 2, 3, 4, 4, 4, 5, 5]
# Output: [1, 2, 3, 4, 5]

# Input: arr[] = [1, 2, 3]
# Output: [1, 2, 3]
# Explanation : No change as all elements are distinct.

arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]

def remDuplicates(a):
    
    if not a:
        return []
    
    res = [a[0]]
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            res.append(a[i])
    return res
                
print(remDuplicates(arr))





# Without append method

arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]

def remDuplicates(a):
    
    if not a:
        return []
    
    res = [0] * len(a)
    res[0] = a[0]
    pos = 1
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            res[pos] = a[i]
            pos += 1
    return res[:pos]

# Why result[:pos]?

# result[:pos] means “take the list from index 0 up to (but not including) index pos”.

# So:

# result[:5] → [1, 2, 3, 4, 5]

# If we didn’t slice, we would return unwanted zeros: [1, 2, 3, 4, 5, 0, 0, 0, 0].
                
print(remDuplicates(arr))