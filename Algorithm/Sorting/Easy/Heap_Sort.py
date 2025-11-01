def heapify(arr, n, i):
    # Maintains max-heap property
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Compare with left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Compare with right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If root not largest, swap and heapify down
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def build_max_heap(arr):
    n = len(arr)
    # Start from last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heap_sort(arr):
    n = len(arr)

    # Step 1: Build max heap
    build_max_heap(arr)

    # Step 2: Extract elements from heap one by one
    for end in range(n - 1, 0, -1):
        # Move current max (root) to end
        arr[0], arr[end] = arr[end], arr[0]

        # Heapify reduced heap
        heapify(arr, end, 0)


# -------------------------------
# 🚀 Example Execution
# -------------------------------
# arr = [4, 10, 3, 5, 1]
arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
print("Original Array:", arr)

heap_sort(arr)

print("Sorted Array:", arr)
