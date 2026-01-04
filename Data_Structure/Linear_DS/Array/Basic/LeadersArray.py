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

def isLeader(a):
    n = len(a)
    max_from_right = a[-1]
    
    print(max_from_right)       # last element is always a leader
    
    for i in range(n-2, -1, -1):
        if a[i] > max_from_right:
            print(a[i])
            max_from_right = a[i]

isLeader(a)

    