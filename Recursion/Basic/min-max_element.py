# Find the minimum/maximum element in a list recursively

def min_max(s,n,val):
    if n < 0:
        return "Max value is", val
    else:
        print(s[n])
        if s[n] >= val:
            val = s[n]
        return min_max(s,n-1,val)
        
list = [1, 4, 300, -5, -4, 8, 6, -100]
n = len(list)
val = list[n-1]
print(min_max(list,n-2,val))