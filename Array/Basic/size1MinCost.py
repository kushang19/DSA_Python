# Minimum cost to make array size 1 by removing larger of pairs

# Problem in plain words

# You have an array.
# Repeatedly pick any two numbers → remove the larger one.
# The cost of that removal = the smaller one of the pair.
# Continue until only one element is left.
# Find the minimum total cost of all these operations.


# Example Walkthrough

# Input: [4, 3, 2]
# Pair (4, 2) → remove 4, cost = 2 → new array [3, 2]
# Pair (3, 2) → remove 3, cost = 2 → new array [2]
# ✅ Total cost = 2 + 2 = 4


a = [4 ,3 ,2 ]
# a = [ 3, 4 ]
# print(a)
n = len(a)
for i in range(n):
    for j in range(i+1,n):
        # print(i,j)
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
b=a
print(b[0])
print(n-1)
cost = b[0] * (n-1)
print("cost = ",cost)