# 🧠 2. Selection Sort — “Find min, place it in front”

# Find the smallest element in the unsorted part and swap it to the front.
# After each pass → the front (left side) becomes sorted.


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)
    return arr

# Example
arr = [64, 25, 12, 22, 11]
print("Selection:", selection_sort(arr))




# 📝 Note

# i and min_idx are swaped at every itertaion ****
# Passes = n-1
# Comparisons: Entire unsorted part
# Swaps = n-1
# Not stable ❌ (because of swaps)
# Time: O(n²), Space: O(1)


# 🎯 Visual tag
# “Select the smallest, fix it at the start — like arranging trophies one by one.”