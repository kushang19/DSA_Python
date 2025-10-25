# Two Sum in sorted array using Two Pointers Technique
# arr = [10, 20, 35, 50] #target 70
arr = [1,2,3,5,7,10,11,15]
target = 15

def two_pointer(arr,target):
    n = len(arr)
    left = 0
    right = n-1

    while(left < right):
        sum = arr[left] + arr[right]
        if sum == target:
            print(left,right)
            return (left,right)
        elif sum > target:
            right-= 1
        else:
            left+= 1

    print(-1)


two_pointer(arr,target)