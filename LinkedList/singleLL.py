# https://www.youtube.com/watch?v=qp8u-frRAnU

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        temp = self.head
        llstr = ""
        while temp:
            llstr += str(temp.data) + "-->"
            # print("start temp ", temp.next, temp.data)
            temp = temp.next

        print(llstr)


    # Why while temp and not while temp.next?

    # while temp: processes every node, including the last one.

    # while temp.next: would stop at the last node, but would not process it. We use this in insert_at_end because we needed to find the last node, not process it.
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data,None)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def remove_at(self,index):
        if index<0 or index>= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return 
        
        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                temp.next = temp.next.next
                break
            temp = temp.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_begining(data)

        count = 0
        temp = self.head

        while temp:

            if count == index - 1:
                node = Node(data, temp.next)
                temp.next = node
                break

            temp = temp.next
            count += 1
 

ll = LinkedList()
ll.insert_at_begining(5)
ll.insert_at_begining(89)
ll.insert_at_begining(100)
ll.insert_at_end(98700)
ll.insert_values(["apple","orange","banana","cheery"])
ll.print()
# ll.remove_at(3)
ll.insert_at(3,"grapes")
ll.print()
print("length ", ll.get_length())