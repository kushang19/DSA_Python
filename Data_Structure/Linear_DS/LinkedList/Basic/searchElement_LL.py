# Search an element in a Linked List

# Given a head of linked list and a key, determine whether the key exists by traversing through the nodes sequentially.

# Search an element in a Linked List

# Given a head of linked list and a key, determine whether the key exists by traversing through the nodes sequentially.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next 
        
class LL:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp = temp.next
        print("\n")
        
    def search(self, key):
        # print("search", key)
        temp = self.head 
        match = False
        while temp:
            if temp.data == key:
                print("Match Found for key ", key)
                match = True
                return 
            temp = temp.next
        if match == False:
            print("Match Not Found")


l = LL()
n1 = Node(1)
l.head = n1
n2 = Node(2)
n1.next = n2
n3 = Node(3)
n2.next = n3
n4 = Node(4)
n3.next = n4
n5 = Node(5)
n4.next = n5
l.display()
l.search(9)