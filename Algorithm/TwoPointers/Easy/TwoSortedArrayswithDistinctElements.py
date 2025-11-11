# Intersection of Two Sorted Arrays with Distinct Elements

# Given two sorted arrays a[] and b[] with distinct elements of size n and m respectively, the task is to find intersection (or common elements) of the two arrays. We need to return the intersection in sorted order.

# Note: Intersection of two arrays can be defined as a set containing distinct common elements between the two arrays.

# Examples:

# Input: a[] = { 1, 2, 4, 5, 6 }, b[] = {  2, 4, 7, 9 }
# Output: { 2, 4 }
# Explanation: The common elements in both arrays are 2 and 4.

# Input: a[] = { 2, 3, 4, 5 }, b[] = { 1, 7 }
# Output: { }
# Explanation: There are no common elements in array a[] and b[].

# a = [1,2,4,5,6]
# b = [2,4,7,9]


# Approach : 

# The idea is to sort both the arrays and then maintain a pointer at the beginning of each array. By comparing the elements at both pointers, we can decide how to proceed:

# If the element in the first array is smaller than the one in the second, move the pointer in the first array forward, because that element can't be part of the intersection. 
# If the element in the first array is greater, move the second pointer forward. 
# If the two elements are equal, you add that element to the result and move both pointers forward. 
# This continues until one of the pointers reaches the end of its array.

a =  [ 2, 3, 4, 5 ] 
b =  [ 1, 2, 7 ]

def arr_checker(a,b):
    n = len(a)
    m = len(b)
    s1 = 0
    s2 = 0
    c = []
    while s1 < n and s2 < m:
        if a[s1] < b[s2]:
            s1+=1
        elif a[s1] > b[s2]:
            s2+=1
        else:
            c.append(a[s1])
            s1+=1
            s2+=1
    
    print(c)

arr_checker(a,b)