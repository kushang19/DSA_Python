class HashTable:
    def __init__(self):
        self.MAX_SIZE = 100
        self.arr = [None for i in range(self.MAX_SIZE)] # List Comprehension in Python
    
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX_SIZE
    
    # def add(self, key, val):
    #     h = self.get_hash(key)
    #     self.arr[h] = val
    #     return self.arr 
    
    # def get(self,key):
    #     h = self.get_hash(key)
    #     return self.arr[h]


    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
        # print(self.arr)
        # return self.arr 
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None



t = HashTable()
print(t.get_hash("march 6"))
# print(t.add("march 6", 130))
# print(t.get("march 6"))

t["sept 30"] = 129
t["april 23"] = 301
t["dec 19"] = 230
print(t["dec 19"])
print(t["march 6"])
print(t.arr)

del t["dec 19"]

print(t.arr)

        