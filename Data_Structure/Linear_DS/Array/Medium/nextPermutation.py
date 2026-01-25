# arr = [2, 4, 1, 7, 5, 0]
# Output: [2, 4, 5, 0, 1, 7]

arr = [1, 3, 5, 4, 2]
# Output: [1, 4, 2, 3, 5]

# arr = [3, 2, 1]
# Output: [1, 2, 3]


def nextPermutation(a):
    n = len(a)

    # Step 1: Find pivot index
    id_1 = -1
    for i in range(n-1, 0, -1):   # ✅ stop at 1
        if a[i] > a[i-1]:
            id_1 = i-1
            break

    # If pivot not found -> reverse whole array (last permutation)
    if id_1 == -1:
        return a[::-1]

    # Step 2: Find next bigger element (from right side)
    id_2 = -1
    for j in range(n-1, id_1, -1):
        if a[j] > a[id_1]:
            id_2 = j
            break

    # Step 3: Swap
    a[id_1], a[id_2] = a[id_2], a[id_1]

    # Step 4: Reverse suffix (fastest)
    a[id_1+1:] = reversed(a[id_1+1:])

    return a



# My solution --- which is not fully correct 

# def nextPermutation(a):
#     for i in range(len(a)-1, -1, -1):
#         if a[i] > a[i-1]:
#             id_1 = i-1
#             break_point = a[i-1]
#             left = a[:i]
#             right = a[i:]
#             min_diff = float('inf') 
#             for j in range(len(right)):

#                 if (right[j] - break_point) <  min_diff and break_point < right[j]:
#                     min_diff = right[j] - break_point
#                     id_2 = len(left)  + j 
    
#             break

#     a[id_1], a[id_2] = a[id_2], a[id_1]
#     left = a[:i]
#     right = a[i:]
#     right.sort()
#     return (left + right)

print(nextPermutation(arr))