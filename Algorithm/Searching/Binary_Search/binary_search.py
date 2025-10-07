# binary_search using recurion

def binary_search(a, k):
    def helper(s, e):
        print(s,e)
        if s > e:
            return -1  # base case: not found

        mid = (s + e) // 2

        if a[mid] == k:
            return mid
        elif a[mid] > k:
            return helper(s, mid - 1)
        else:
            return helper(mid + 1, e)

    return helper(0, len(a) - 1)


# Example tests
a = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# print(binary_search(a, 12))   # ✅ 11
# print(binary_search(a, 1))    # ✅ 0
print(binary_search(a, -3))   # ✅ 12
print(binary_search(a, 100))  # ✅ -1
