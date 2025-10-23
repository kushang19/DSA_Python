# Note: Dictionary uses built in hash table methods, it hashs key on its own and if collision occurs it uses open addressing - qudratic method 


my_dictionary = {}

my_dictionary["a"] = "kushang"
my_dictionary["b"] = "atul"
my_dictionary["c"] = "ganesh"
my_dictionary["d"] = "vishal"
my_dictionary["e"] = "sahil"

print(my_dictionary)

print("value:",my_dictionary["a"])

del my_dictionary['b']

print(my_dictionary)