# Length of a Linked List

# Given a Singly Linked List, the task is to find the Length of the Linked List.

# Examples:

# Input: LinkedList = 1->3->1->2->1
# Output: 5
# Explanation: The linked list has 5 nodes.

# Input: LinkedList = 2->4->1->9->5->3->6
# Output: 7 
# Explanation: The linked list has 7 nodes.

# Input: LinkedList = 10->20->30->40->50->60
# Output: 6
# Explanation: The linked list has 6 nodes.


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
            count = 0
            temp = self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp = temp.next
                count +=1
            print("\n")
            print("count =",count)

l = LL()
# l.display()
n1 = Node(1)
l.head = n1
n2 = Node(3)
n1.next = n2
n3 = Node(1)
n2.next = n3
n4 = Node(2)
n3.next = n4
n5 = Node(1)
n4.next = n5
l.display()
