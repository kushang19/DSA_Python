def rotate_left(a, d):
    n = len(a)
    d = d % n  # Handle d > n
    return a[d:] + a[:d]

print(rotate_left([1,2,3,4,5], 2))


def rotate_right(a, d):
    n = len(a)
    d = d % n
    return a[n-d:] + a[:n-d]





# Step 1: What happens if we rotate 12 times?

# After 5 rotations → same
# After 10 rotations → same

# So 12 rotations =

# 10 full cycles + 2 more rotations


# So effectively it is just 2 rotations.

# Step 2: Using d % n
# d = 12 % 5 = 2


# So instead of rotating 12 times,
# we rotate only 2 times → same result, faster, correct.