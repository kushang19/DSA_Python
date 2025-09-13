# Anti-Clockwise

a = [1,2,3,4,5]
# Output: [3, 4, 5, 1, 2]
d = 2

def rotateArrays(a,d):
    n = len(a)
    res = [0] * n
    # print(res)
    
    for i in range(n):
        if i+d > n-1:
            d = -(n-d)
        res[i] = a[i+d]
        print(i,i+d)
        # print(a)
    print(res)

rotateArrays(a,d)


#Clockwise

a = [1, 2, 3]

# Output: {3, 1, 2}
d = 4

def rotateArrays(a,d):
    n = len(a)
    res = [0] * n
    # print(res)
    
    for i in range(n):
        cw = n - d 
        # print(i,cw)
        res[i] = a[cw]
        if cw < n-1:
            d = d - 1
        else:
            d = n
    print(res)

rotateArrays(a,d)