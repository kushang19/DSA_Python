# Write a function to get Nth node in a Linked List

# Given a LinkedList and an index (1-based). The task is to find the data value stored in the node at that kth position. If no such node exists whose index is k then return -1.

# Example: 

# Input:  1->10->30->14,  index = 2
# Output: 10
# Explanation: The node value at index 2 is 10


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
        temp = self.head 
        match = False
        count = 1
        while temp:
            if temp.data == key:
                print(key, "Key Found at positon", count)
                match = True
                return 
            temp = temp.next
            count +=1
        if match == False:
            print("Match Not Found")

    def deleteLL(self):
        self.head = None


l = LL()
n1 = Node(1)
l.head = n1
n2 = Node(10)
n1.next = n2
n3 = Node(30)
n2.next = n3
n4 = Node(14)
n3.next = n4
n5 = Node(50)
n4.next = n5
l.search(50)
l.display()

# Write a function to delete a Linked List
l.deleteLL()
l.display()