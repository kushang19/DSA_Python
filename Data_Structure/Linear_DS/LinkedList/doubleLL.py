# DISPLAY DDL  
# https://www.youtube.com/watch?v=89Gma338jHU 

# INSERTION AT BEGINNING,ENDING AND SPECIFIED POSITION DDL
# https://www.youtube.com/watch?v=JeS4povWMAQ 

# DELETION AT BEGINNING,ENDING AND SPECIFIED POSITION
# https://www.youtube.com/watch?v=UADuKgCraaY



class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print("Empty Double Linked List")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next

    def insert_at_beginning(self, data):
        n = Node(data)
        temp = self.head
        temp.prev = n
        n.next = temp
        self.head = n

    def insert_at_end(self, data):
        n = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.next = n
        n.prev = temp

    def insert_at_position(self, pos, data):
        n = Node(data)
        temp = self.head
        for i in range(1, pos-1):
            temp = temp.next
        
        n.prev = temp
        n.next = temp.next
        temp.next.prev = n
        temp.next = n

    def delete_at_beginning(self):
        temp = self.head
        self.head = temp.next
        self.head.prev = None
        temp.next = None

    def delete_at_end(self):
        before = self.head
        temp = self.head.next

        while temp.next is not None:
            temp = temp.next
            before = before.next
        
        before.next = None
        temp.prev = None

    def delete_at_position(self, pos):
        temp = self.head.next
        before = self.head

        for i in range(1,pos-1):
            temp = temp.next
            before = before.next

        before.next = temp.next
        temp.next.prev = before

        temp.next = None
        temp.prev = None



        
l = DLL()
n1 = Node(10)
l.head = n1
n2 = Node(20)
n1.next = n2
n2.prev = n1
n3 = Node(30)
n2.next = n3
n3.prev = n2
n4 = Node(40)
n4.prev = n3
n3.next = n4
n5 = Node(50)
n5.prev = n4
n4.next = n5
# l.insert_at_beginning(5)
# l.insert_at_end(60)
# l.insert_at_end(70)
l.insert_at_position(3,25)
l.delete_at_beginning()
l.delete_at_end()
l.delete_at_position(3)
l.display()