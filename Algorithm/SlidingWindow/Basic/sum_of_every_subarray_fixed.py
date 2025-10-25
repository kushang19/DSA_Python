# Sum of every subarray of size k (fixed-size window)
arr = [2, 1, 3, 4, 6] 
k = 3

def sums_of_size_k(arr, k):
    s = 0
    res = []
    n = len(arr)
    for i in range(k):
        s += arr[i]
    res.append(s)
    print(res)
    for i in range(1, n-k+1):
        s = s - arr[i-1] + arr[n-k+i]
        res.append(s)

    print(res)

sums_of_size_k(arr, k)