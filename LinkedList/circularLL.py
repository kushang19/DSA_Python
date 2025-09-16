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
            self.tail = n # make sure to make 'n' as tail
            self.tail.next = self.head
    
    def insert_at_position(self,pos,data):
        temp = self.head
        n = Node(data)
        if self.head is None:
            self.head = n
            self.tail = n
            self.tail.next = self.head 
        else:
            if pos == 1:
                self.insert_at_beginning(data)
            else:
                for i in range(1,pos-1):
                    temp = temp.next

                n.next = temp.next
                temp.next = n


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

l.insert_at_beginning(5)
l.insert_at_end(35)
l.insert_at_end(45)

l.insert_at_position(1,25)

l.display()