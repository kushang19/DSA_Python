# Sum of all Subarrays

# Input: arr[] = [1, 4, 5, 3, 2]
# Output: 116
# Explanation: Sum of all possible subarrays of the array [1, 4, 5, 3, 2] is 116.

# Input: arr[] = [1, 2, 3, 4]
# Output: 50
# Explanation: Sum of all possible subarrays of the array [1, 2, 3, 4] is 50.

# Method : O(n^3)
def sum_subArray(a):

    n = len(a)
    sum = 0

    # picking start point
    for i in range(n):
        # picking end point
        for j in range(i,n):
            # sub arrays between start and end
            for k in range(i, j+1):
                print(a[k],end=" ")
                sum += a[k]
            print()
    return sum

arr = [1,2,3,4]
print("sum of sub array is M1 : ",sum_subArray(arr))


# Method: O(n^2)

def sum_sub_array(a):
    n = len(a)
    result = 0

    for i in range(n):
        temp = 0
        for j in range(i,n):
            temp += a[j]
            result += temp

    return result

arr = [1,2]
print("sum of sub array is M2 : ",sum_sub_array(arr))



# Method: O(n)

def sum_sub_array_n(a):
    n = len(a)
    result = 0

    for i in range(n):
        result += a[i] * (i+1) * (n-i)

    return result

arr = [1,2,3,4]
print("sum of sub array is M3 : ",sum_sub_array_n(arr))