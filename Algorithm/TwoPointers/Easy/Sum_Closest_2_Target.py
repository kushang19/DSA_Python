# 2 Sum - Pair Sum Closest to Target

# Input: arr[] = [5, 2, 7, 1, 4], target = 10

# Output: [2, 7]
# Explanation: As (4, 7) and (2, 7) both are closest to 10, but absolute difference of (2, 7) is 5 and 
# (4, 7) is 3. Hence, [2, 7] has maximum absolute difference and closest to target.

# absolute difference win (i.e., |a - b| is largest).


arr = [5, 2, 7, 1, 4]
target = 10


def closest_pair(arr,target):
    n = len(arr)
    arr.sort()
    res = []
    minDiff = float('inf')
    s = 0
    e = n - 1

    # check closest pair

    while s < e:
        currSum = arr[s] + arr[e]

        if abs(target - currSum) < minDiff:
            minDiff = abs(target - currSum)
            res = [arr[s], arr[e]]

        if currSum < target:
            s+=1
        elif currSum > target:
            e-=1
        else:
            return res

    return res 
       

res =  closest_pair(arr,target)
if len(res) > 0:
    	print(res[0], res[1])