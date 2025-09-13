# Minimum increment by k operations to make all equal

# Input: arr = [4, 7, 19, 16], k = 3

# Minimum = 4, Maximum = 19

# Check divisibility:
# (7−4) % 3 = 0 ✅
# (19−4) % 3 = 0 ✅
# (16−4) % 3 = 0 ✅

# All good → possible.

# Count steps:

# 4 → needs (19−4)/3 = 5 steps
# 7 → needs (19−7)/3 = 4 steps
# 19 → needs (19−19)/3 = 0 steps
# 16 → needs (19−16)/3 = 1 steps

# Total = 5+4+0+1 = 10 operations ✅


# Note 
# 1. Pick the minimum element as a reference.
# 2. Check (arr[i] − min) % k == 0 for all i.
# 3. If all pass → possible. Otherwise → -1.



a = [4, 7, 19, 16]
# a = [4, 4, 4, 4]
k = 3
n = len(a)

# Sorting logic...
for i in range(n):
    for j in range(i+1,n):
        # print(i,j)
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

b = a
# print(a, b)    

min = b[0]
max = b[n-1]

print(min,max)

c = 0
for i in range(1,n):
    if((b[i] - min) % k == 0):
        continue
    else:
        c = True
        break
        
if(c):
    print("Not Possible")
else:
    print("Possible")
    
opr = 0
for i in range(n):
    opr += (max - b[i])/k
print("Operations =",opr)