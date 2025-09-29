# Check if an array is sorted (strictly increasing) using recursion
# Input: [1, 2, 3, 5, 7] → True
# Input: [1, 5, 3, 4] → False


def sorted_array(a,n,i,v):
    if i > n:
        return True
    else:
        # print("a[i] and v",a[i],v)
        if v > a[i]:
            return False
        else:
            # print("a[i]=",a[i])
            v = a[i]
            # print("v=",v)
            return sorted_array(a,n,i+1,v)


a = [1, 2, 3, 5, 7]
n = len(a)
v = a[0]
i=1

print(sorted_array(a,n-1,i,v))