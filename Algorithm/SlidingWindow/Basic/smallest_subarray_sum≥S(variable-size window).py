# Smallest subarray with sum ≥ S (variable-size window)

arr = [2,1,5,2,3,2]
S = 7
def smallest_subarray_with_sum_ge(arr, S):
    s = 0
    start = 0
    n = len(arr)
    min_len = float("inf")

    for end in range(n):
        s+= arr[end]
        while s >= S:
            min_len = min(min_len, end - start + 1)
            s -= arr[start]
            start+=1
    
    return -1 if min_len == float('inf') else min_len


print(smallest_subarray_with_sum_ge(arr, S)) 