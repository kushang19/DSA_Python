# Reverse a string preserving space positions using Two Pointers Technique 

# Given a string s, the task is to reverse the given string while preserving the position of spaces.

# Examples: 

# Input: "internship at geeks for geeks"
# Output: skeegrofsk ee gtapi hsn retni
# Explanation : Reversing the characters without spaces "skeegrofskeegtapihsnretni" and inserting space at original place"skeegrofsk ee gtapi hsn retni"



def preserveSpace(Str):
    n = len(Str)
    Str = list(Str)

    start = 0
    end = n -1

    while (start < end):
        if (Str[start] == " "):
            start += 1
            continue
        elif (Str[end] == " "):
            end -= 1
            continue
        else:
            Str[start], Str[end] = (Str[end], Str[start])
            start += 1
            end -= 1
    
    return (''.join(Str))

Str = "internship at geeks for geeks"
print(preserveSpace(Str))













# Remove All Occurrences of an Element in an Array using Two Pointers Technique 

# Problem Statement:
# Given an integer array arr[] and an integer ele the task is to the remove all occurrences of ele from arr[] in-place and return the number of elements which are not equal to ele

# Input: arr[] = [0, 1, 3, 0, 2, 2, 4, 2], ele = 2
# Output: 5
# Explanation: The answer is 5 because there are 5 elements which are not equal to 2 and arr[] will be modified such that the first 5 elements contain the elements which are not equal to 2 and remaining elements can contain any element. 
# So, modified arr[] = [0, 1, 3, 0, 4, _, _, _]


# arr = [3, 2, 2, 3]
# arr = [0, 1, 3, 0, 2, 2, 4, 2]
# ele = 2

# def remove_occ(arr,ele):
#     count = 0
#     res = []
#     for i in range(len(arr)):
#         if arr[i] != ele:
#             count += 1
#             res.append(arr[i])
#     for _ in range(len(arr) - count):
#         res.append('_')
#     print(count)
#     print(res)


# remove_occ(arr, ele)





