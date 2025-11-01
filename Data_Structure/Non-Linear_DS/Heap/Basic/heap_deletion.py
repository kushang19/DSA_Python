def heapify(arr, n, i, level=0):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i :
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr,n,largest,level+1)


def min_heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left
    
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)



def build_max_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr,n,i)
    return arr

# delete 

# def delete_root_max_heap(arr):
#     n = len(arr)
#     if n == 0:
#         print("Heap is empty.")
#         return []

#     #This is tuple unpacking in Python — a compact way to swap two values without using a temp variable.
#     arr[0], arr[-1] = arr[-1], arr[0]  

#     # Step 2: Remove last element (previous root)
#     root = arr.pop()

#     # Step 3: Heapify down from root to fix heap
#     heapify(arr, len(arr), 0)

#     return arr


# Without In built popup method 
def delete_root_manual(arr):
    n = len(arr)
    if n == 0:
        print("Heap is empty")
        return arr

    # Step 1: Swap root and last element
    arr[0], arr[n - 1] = arr[n - 1], arr[0]

    # Step 2: Copy all elements except the last one to simulate deletion
    new_heap = [arr[i] for i in range(n - 1)]

    # The line in step 2 means

    # new_heap = []
    # for i in range(n - 1):
    #     new_heap.append(arr[i])



    # Step 3: Heapify from the root again
    heapify(new_heap, len(new_heap), 0)

    return new_heap



# ======= MAIN =====

arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]

print("Original Array:",arr)

max_heap = build_max_heap(arr)

print("Final Max Heap Array:",max_heap)

# Perform Deletion
max_heap = delete_root_manual(max_heap)
print("\nAfter Deletion (New Max Heap):", max_heap)

# print_heap_tree(max_heap)
