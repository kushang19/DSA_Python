class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SLL:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Empty Singly Linked List")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next
            print()

    def insert_at_beginning(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def insert_at_end(self, data):
        n = Node(data)
        if self.head is None:
            self.head = n
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = n

    def insert_at_position(self, pos, data):
        if pos == 1:
            self.insert_at_beginning(data)
            return

        n = Node(data)
        temp = self.head

        for i in range(1, pos - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        n.next = temp.next
        temp.next = n

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None

    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def delete_at_position(self, pos):
        if self.head is None:
            print("List is empty")
            return

        if pos == 1:
            self.delete_at_beginning()
            return

        temp = self.head
        for i in range(1, pos - 1):
            if temp.next is None:
                print("Position out of range")
                return
            temp = temp.next

        to_delete = temp.next
        if to_delete is None:
            print("Position out of range")
            return
        
        temp.next = to_delete.next
        to_delete.next = None


# ✅ Example usage:
l = SLL()
n1 = Node(10)
l.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
n4 = Node(40)
n3.next = n4
n5 = Node(50)
n4.next = n5

# Test operations
l.insert_at_beginning(5)
l.insert_at_end(60)
l.insert_at_position(3, 25)
l.delete_at_beginning()
l.delete_at_end()
l.delete_at_position(4)
l.display()




# if self.head.next is None:
#     self.head = None
#     return

# ✔ Checks if there’s only one node in the list
# ✔ If yes, delete it by setting head = None
# ✔ Then stop the function immediately
# ✔ Prevents errors and handles edge cases safely