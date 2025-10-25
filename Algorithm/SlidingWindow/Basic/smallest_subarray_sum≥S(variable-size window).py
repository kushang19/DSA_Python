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



# 🪄 Step-by-step “Animation” of "abca"


# | Step | `end` | `s[end]` | Window (s[start:end]) | `freq` changes            | Action                             | `max_len` |
# | ---- | ----- | -------- | --------------------- | ------------------------- | ---------------------------------- | --------- |
# | 1    | 0     | 'a'      | `'a'`                 | freq['a']=1               | no duplicate                       | 1         |
# | 2    | 1     | 'b'      | `'ab'`                | freq['b']=1               | no duplicate                       | 2         |
# | 3    | 2     | 'c'      | `'abc'`               | freq['c']=1               | no duplicate                       | 3         |
# | 4    | 3     | 'a'      | `'abca'`              | freq['a']=2 ⚠️ duplicate! | start=0 → remove 'a' (freq['a']=1) | 3         |
