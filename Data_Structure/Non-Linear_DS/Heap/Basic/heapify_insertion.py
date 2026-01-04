def heapify(arr, n, i, level=0):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Find largest among root and children
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If root is not largest, swap and continue heapifying
    if largest != i:
        print(f"{'  '*level}Swap: {arr[i]} ↔ {arr[largest]}")
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, level+1)


def build_max_heap(arr):
    n = len(arr)
    # Start from last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        print(f"\nHeapify called on index {i} (value={arr[i]}):")
        heapify(arr, n, i)
        print(f"After heapify({i}): {arr}")
    return arr


def print_heap_tree(arr):
    """Print heap in a tree-like structure for clarity"""
    print("\nHeap Tree Structure:\n")
    level = 0
    next_level = 2 ** level
    for i, val in enumerate(arr):
        print(f"{val}", end="  ")
        if i + 1 == next_level:
            print("\n")
            level += 1
            next_level += 2 ** level
    print("\n")


# -------------------------------
# 🚀 Example Execution
# -------------------------------
arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]

print("Original Array:")
print(arr)

max_heap = build_max_heap(arr)

print("\n✅ Final Max Heap Array:")
print(max_heap)

# print_heap_tree(max_heap)
