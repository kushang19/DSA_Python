# Given an array arr[] of size n, the task is to find all the Leaders in the array. An element is a Leader if it is greater than or equal to all the elements to its right side.

# Note: The rightmost element is always a leader.

# Examples:

# Input: arr[] = [16, 17, 4, 3, 5, 2]
# Output: [17 5 2]
# Explanation: 17 is greater than all the elements to its right i.e., [4, 3, 5, 2], therefore 17 is a leader. 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.

# Input: arr[] = [1, 2, 3, 4, 5, 2]
# Output: [5 2]
# Explanation: 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.


a = [16, 17, 4, 3, 5, 2]
# a = [1, 2, 3, 4, 5, 2]
# Output: [17 5 2]
def isLeader(a):
    n = len(a)
    for i in range(0,n):
        res = 0
        for j in range(i+1, n):
            if(a[i] >= a[j]):
                res = 1
            else:
                res = -1
                break
        if(res == 1):
            print(a[i])
    print(a[n-1])

isLeader(a)
    