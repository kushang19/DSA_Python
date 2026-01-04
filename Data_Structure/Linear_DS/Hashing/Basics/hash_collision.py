class HashTable:
    def __init__(self):
        self.MAX_SIZE = 10
        self.arr = [[] for _ in range(self.MAX_SIZE)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX_SIZE

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            print('------------------------', idx, element, len(element), element[0])
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            # print("element: ",element[0],"key:",key)
            if element[0] == key:
                del self.arr[h][idx]
                break

# ------------------ Testing ------------------

t = HashTable()

t["march 6"] = 120  # updates later
t["march 6"] = 78
t["march 8"] = 67
t["march 9"] = 4
t["march 17"] = 459

print(t.arr)   # ✅ This is what creates the visual like your screenshot
print(t["march 6"])

del t["march 17"]
print(t.arr)

        



# =============================== Enumerate() in Python ================================
#                                 v^v^v^v^v^v^v^v^v^v^v^

# https://www.geeksforgeeks.org/python/enumerate-in-python/



# enumerate() function adds a counter to each item in a list or any other iterable, and returns a list of tuples containing the index position and the element for each element of the iterable.

# It turns the iterable into something we can loop through using indexes, where each item comes with its number (starting from 0 by default).

# Let's look at a simple example of an enumerate() with a list.


# a = ["Geeks", "for", "Geeks"]

# # Iterating list using enumerate to get both index and element
# for i, name in enumerate(a):
#     print(f"Index {i}: {name}")

# # Converting to a list of tuples
# print(list(enumerate(a)))


# Output

# Index 0: Geeks
# Index 1: for
# Index 2: Geeks
# [(0, 'Geeks'), (1, 'for'), (2, 'Geeks')]