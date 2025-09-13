# Given an array arr[], check if it is sorted in ascending order or not. Equal values are allowed in an array and two consecutive equal values are considered sorted.

# Input: arr[] = [10, 20, 30, 40, 50]
# Output: true
# Explanation: The given array is sorted.

# Input: arr[] = [90, 80, 100, 70, 40, 30]
# Output: false
# Explanation: The given array is not sorted.

arr = [90, 80, 100, 70, 40, 30]

def sortedArray(a):
    n = len(a)
    for i in range(0,n):
        for j in range(i+1,n):
            if(a[i] <= a[j]):
                continue
            else:
                return False
    return True
            
print(sortedArray(arr))