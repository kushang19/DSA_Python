class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class CLL:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print("CLL is Empty")
        else:
            temp = self.head
            print(temp.data,'-->',end=" ")
            while temp.next != self.head:
                temp = temp.next
                print(temp.data,'-->',end=" ")
            print(temp.next.data)
    
    def insert_at_beginning(self,data):
        n = Node(data)
        if self.head is None:
            self.head = n
            self.tail = n
            self.tail.next = self.head
        else:
            n.next = self.head
            self.tail.next = n
            self.head = n

    def insert_at_end(self, data):
        n = Node(data)
        if self.head is None:
            self.head = n
            self.tail = n
            self.tail.next = self.head 
        else:
            self.tail.next = n
            self.tail = n
            n.next = self.head
            
    def insert_at(self, data, pos):
        n = Node(data)
        if self.head is None:
            self.head = n
            self.tail = n
            self.tail.next = self.head
        else:
            temp = self.head
            for i in range(1, pos-1):
                temp = temp.next
            n.next = temp.next
            temp.next = n
    
    def delete_at_beginning(self):
        temp = self.head
        self.head = temp.next
        self.tail.next = self.head
        
    def delete_at_end(self):
        if self.head == self.tail:
            self.tail = None
            self.head = None
            return
        
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        
        self.tail = temp 
        temp.next = self.head
        
    
    def get_length(self):
        if self.head is None:
            return 
        else:
            temp = self.head 
            count = 1
            while temp.next != self.tail.next:
                temp = temp.next
                count += 1
            
            print("count=", count)
            return count
        

    def delete_at_pos(self,pos):
        if pos == 0:
            self.delete_at_beginning()
        
        if pos > self.get_length():
            print("Invalid Index")
            return
        
        temp = self.head
        for i in range(1,pos-1):
            temp = temp.next 
        
        temp.next = temp.next.next

l = CLL()
n1 = Node(10)
l.head = n1
l.tail = n1
l.tail.next = l.head

n2 = Node(20)
l.tail.next = n2
l.tail = n2
l.tail.next = l.head

n3 = Node(30)
l.tail.next = n3
l.tail = n3
l.tail.next = l.head

l.insert_at_beginning(0)
l.insert_at_end(40)
l.insert_at(25,4)

l.display()
l.get_length()

l.delete_at_beginning()
l.display()
l.get_length()

l.delete_at_end()
l.display()
l.get_length()

l.delete_at_pos(3)
l.display()
l.get_length()