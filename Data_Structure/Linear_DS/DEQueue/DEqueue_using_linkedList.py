# =================================== DEQueue using Linked Lists ====================================

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SLL:
    def __init__(self):
        self.head = None

    def enqueueF(self, data):
        node = Node(data, self.head) # while creating a NodeB after NodeA is created, NodeB(data=20, next=NodeA)
        self.head = node

    def enqueueR(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            temp = self.head 
            while temp.next:
                temp = temp.next
            temp.next = node
    
    def dequeueF(self):
        if self.head is None:
            print("Queue is Empty")
        else:
            self.head = self.head.next
    
    def dequeueR(self):
        if self.head is None:
            print("Queue is Empty")
        else:
            n = self.get_length()
            print("n =", n)
            if n <= 1:
                self.head = None
            else:
                temp = self.head
                for i in range(n-2):
                    # print(i)
                    temp = temp.next
                # print("out side for", temp.data)
                temp.next = None

        # else:
        #     temp = self.head
        #     while temp.next.next:
        #         temp = temp.next
        #     print("TEMP ", temp.data)
        #     temp.next = None
    
            

    def get_length(self):
        count = 1
        if self.head is None:
            return 0
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
                count += 1
        return count
        

    def display(self):
        if self.head is None:
            print("Queue is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,end=" ")
                temp = temp.next
    

q = SLL()
q.enqueueF(10)
q.enqueueF(20)
q.enqueueF(30)
q.enqueueF(40)
q.dequeueR()
q.dequeueR()
q.dequeueR()
q.dequeueR()
# q.enqueueF(50)
# q.enqueueR(100)
# q.enqueueR(200)
# q.dequeueF()
# q.dequeueF()
# q.dequeueR()
# q.dequeueR()
# q.dequeueR()
# q.dequeueR()
# q.dequeueR()
# print("length = ", q.get_length())
q.display()
            
        
