# Duplicate within K Distance in an Array

# Given an integer array arr[] and an integer k, determine whether there exist two indices i and j such that arr[i] == arr[j] and |i - j| ≤ k. If such a pair exists, return 'Yes', otherwise return 'No'.

# Examples: 

# Input: k = 3, arr[] = [1, 2, 3, 4, 1, 2, 3, 4]
# Output: No
# Explanation: Each element in the given array arr[] appears twice and the distance between every element and its duplicate is 4.

# Input: k = 3, arr[] = [1, 2, 3, 1, 4, 5]
# Output: Yes
# Explanation: 1 is present at index 0 and 3.

# Input: k = 3, arr[] = [1, 2, 3, 4, 5]
# Output: No
# Explanation: There is no duplicate element in arr[].


def duplicate_within_k(a,k):
    n = len(a)
    for i in range(n):
        # print(i)
        for j in range(i+1,n):
            # print(i,j)
            if (a[i] == a[j]) and (j-i <= k):
                # print(a[i],a[j],"----", i,j,"-----",j-i,"<=", k)
                return "Yes"
            
    return "No"

a = [1, 2, 3, 1, 4, 5]
k = 3
print(duplicate_within_k(a,k))
