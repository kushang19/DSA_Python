# 🧠 3. Insertion Sort — “Insert element into sorted part”

# Take one element from the unsorted part and insert it into its correct position in the sorted part (like sorting cards in your hand).


def insertion_sort(a):
    n = len(a)
    print(a) 
    for i in range(1, n):
        key = a[i]          # current element to insert
        j = i - 1

        # shift elements greater than key to one position ahead
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        print("out while ",a)
        a[j + 1] = key      # insert key at correct position
        print(a)            # for visualization

arr = [16, 15, 4, 13, 2, 1]
insertion_sort(arr)



# 📝 Note

# In Insertion sorting at every iteartion our 'i' gets sorted
# Best case (sorted): O(n) 🟢
# Worst case (reversed): O(n²)
# Stable ✅
# Works great for small or nearly sorted data.
# Time: O(n²), Space: O(1)

# 🎯 Visual tag
# “Sort cards in your hand — pick one, slide it where it belongs.”