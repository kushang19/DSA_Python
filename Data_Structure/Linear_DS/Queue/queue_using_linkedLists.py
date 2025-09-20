
# ============================= Queue(FIFO) using Linked lists ====================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self):
        x = input("Enter your Element :" )
        print('----------------------')
        n = Node(x)
        if self.front is None:
            self.front = n
            self.rear = n
        else:
            self.rear.next = n
            self.rear = n

    def dequeue(self):
        if self.front is None:
            print("QUEUE is EMPTY")
        elif self.front.next is None:  # self.front == self.rear
            print("Popped Element is: ", self.front.data)
            print("---------------------------")
            self.front = None
        else:
            temp = self.front
            print("Popped Element is: ", self.front.data)
            print("---------------------------")
            self.front = temp.next
            temp = None 

    def display(self):
        if self.front is None:
            print("QUEUE is EMPTY")
        else:
            print('THE QUEUE LIST is')
            temp = self.front 
            while temp:
                print(temp.data,end=" ")
                temp = temp.next
            print("\nFront of Queue is: ", self.front.data)
            print("Rear of Queue is: ", self.rear.data)
            print('\n----------------------')
        

q = Queue()

while(1):
    print("Enter the options from below:\n1-enqueue Opretaion\n2-dequeue Opretaion\n3-Display Opretaion\nEnter any key to EXIT Program")
    choice = input()
    if choice == '1':
        print("========== ENQUEUE OPERATION ==========")
        q.enqueue()
        print()
    elif choice == '2':
        print("========== DEQUEUE OPERATION ==========")
        q.dequeue()
        print()
    elif choice == '3':
        print("========== DISPLAY OPERATION ==========")
        q.display()
        print()
    else:
        print("========== EXIT PROGRAM ==========")
        print()
        break