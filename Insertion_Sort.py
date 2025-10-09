# Insertion Sort

# Note: In Insertion sorting at every iteartion our 'i' gets sorted

def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]          # current element to insert
        j = i - 1

        # shift elements greater than key to one position ahead
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key      # insert key at correct position
        print(a)            # for visualization

arr = [16, 15, 4, 13, 2, 1]
insertion_sort(arr)
