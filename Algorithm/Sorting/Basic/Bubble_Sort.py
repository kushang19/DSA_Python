# 🧠 1. Bubble Sort — “Repeatedly push the largest to the end”

# Keep swapping adjacent elements if they are in the wrong order.
# After each full pass → the largest element “bubbles” to the end. *****


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            print("i:",i," ","j:",j)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)
    return arr

# Example
arr = [5, 1, 4, 2, 8]
print("Bubble:", bubble_sort(arr))


# 📝 Note: 

# Passes = n-1
# Comparisons: Adjacent elements
# Largest goes last each pass
# Stable sort ✅
# Time: O(n²), Space: O(1)


# 🎯 Visual tag
# “Like bubbles rising — largest keeps floating to the end after each round.”