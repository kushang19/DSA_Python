# Program for Nth node from the end of a Linked List
    
# Examples:

# Input: 1 -> 2 -> 3 -> 4, N = 3
# Output: 2
# Explanation: Node 2 is the third node from the end of the linked list.

# Input: 35 -> 15 -> 4 -> 20, N = 4
# Output: 35
# Explanation: Node 35 is the fourth node from the end of the linked list.


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
        
    def get_length(self):
        temp = self.head
        count = 1

        while temp.next:
            temp = temp.next
            count += 1
        return count
    
    def search_from_end(self,key):
        n = self.get_length()
        temp = self.head
 
        for i in range(n, 0, -1):
            if key == i:
                print("Output =",temp.data)
                return
            temp = temp.next

        if i <= 1:
            print(-1)



l = LL()
n1 = Node(35)
l.head = n1
n2 = Node(15)
n1.next = n2
n3 = Node(4)
n2.next = n3
n4 = Node(20)
n3.next = n4
l.get_length()
l.search_from_end(4)
l.display()