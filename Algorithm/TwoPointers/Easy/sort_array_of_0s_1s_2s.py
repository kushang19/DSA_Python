# Sort an array of 0s, 1s and 2s - Dutch National Flag Problem

# Given an array arr[] consisting of only 0s, 1s, and 2s. The objective is to sort the array, i.e., put all 0s first, then all 1s and all 2s in last.

# Examples:

# Input: arr[] = [0, 1, 2, 0, 1, 2]
# Output: [0, 0, 1, 1, 2, 2]
# Explanation: [0, 0, 1, 1, 2, 2] has all 0s first, then all 1s and all 2s in last.

arr = [0, 1, 2, 0, 1, 2]

def sort_arry(arr):
    n = len(arr)
    # initialize three pointers:
    # lo: boundary for 0s
    # mid: current element being checked
    # hi: boundary for 2s
    lo = 0
    mid = 0
    hi = n-1

    # process elements until mid crosses hi
    while mid <= hi:
        if arr[mid] == 0:
            # current is 0: swap with lo and move both pointers forward
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo+=1
            mid+=1

        elif arr[mid] == 1:
            # current is 1: it's already in correct position
            mid+=1
            
        else:
            # current is 2: swap with hi and move hi backward do not increment mid, as swapped value needs to be re-checked
            arr[mid],arr[hi] = arr[hi],arr[mid]
            hi-=1
    
    print(arr)

sort_arry(arr)