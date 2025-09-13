# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: [1, 2, 4, 3, 5, 0, 0, 0]

a = [1, 2, 0, 4, 3, 0, 5, 0]

def zeroEnd(a):
    n = len(a)
    z = 0
    pos = 0
    zero = [0] * n
    num = [0] * n
    for i in range(0,n,1):
        if a[i] == 0:
            zero[z] = a[i]
            z += 1
        else:
            num[pos] = a[i]
            pos += 1 
    
    # print(pos,z)
    # print(zero[:z])
    # print(num[:pos])
    print(num[:pos] + zero[:z])
            
zeroEnd(a)