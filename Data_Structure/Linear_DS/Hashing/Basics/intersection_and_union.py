# a = [1,2,3]
# b = [4,5,6]
# #intersection: []
# #union: [1,2,3,4,5,6]

# a = [1, 1, 1]
# b = [1, 1, 1, 1, 1]
#intersection: [1]

a = [1, 2, 3]
b = [3, 4, 5]
#intersection: [3]

# a = [1, 2, 1, 3, 1]
# b = [3, 1, 3, 4, 1]
#intersection: [1,3]


def intersection(a, b):
    freq = {}
    result = []

    # store elements of a
    for x in a:
        freq[x] = 1

    # check elements of b
    for x in b:
        if x in freq and freq[x] == 1:
            result.append(x)
            freq[x] = 0   # avoid duplicates

    return result


print(intersection(a, b))  


def union(a, b):
    freq = {}
    result = []

    for x in a + b:
        if x not in freq:
            freq[x] = 1
            result.append(x)

    return result


print(union(a, b))  

