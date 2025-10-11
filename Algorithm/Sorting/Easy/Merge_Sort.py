a = [2, 8, 5, 3, 9, 4, 1, 7]

def merge_sort(arr):
    if len(arr) <= 1:
        print("arr",arr)
        return arr  # Base case

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # Divide left half
    print('left', left)
    right = merge_sort(arr[mid:])  # Divide right half
    print("right ", right)
    return merge(left, right)      # Conquer (merge)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Merge step (compare and push smaller)
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
        # print("sorted in wile loop ", sorted_arr)

    # Add remaining elements (if any)
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    print("merge ",sorted_arr)  # For visualization
    return sorted_arr

print("Final Sorted Output:", merge_sort(a))




    #            [2,8,5,3,9,4,1,7]
    #             /             \
    #      [2,8,5,3]           [9,4,1,7]
    #      /      \           /        \
    #   [2,8]    [5,3]     [9,4]     [1,7]
    #   /  \     /  \      /  \      /  \
    # [2] [8] [5] [3]   [9] [4]   [1] [7]
    #   ↓     ↓     ↓      ↓       ↓     ↓
    # [2,8] [3,5]  →   [4,9]  [1,7]
    #     ↓             ↓        ↓
    #   [2,3,5,8]     [1,4,7,9]
    #              ↓
    #      [1,2,3,4,5,7,8,9]

