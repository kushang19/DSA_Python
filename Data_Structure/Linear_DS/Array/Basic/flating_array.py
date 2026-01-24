# ======== Flating Array ==========

a = [1,2,[3,7,8,9,[4,[5]]]]
b = []

def flat(list):
    for i in list:
        if isinstance(i, int):
            b.append(i)
        else:
            flat(i)
    return b

print(flat(a))