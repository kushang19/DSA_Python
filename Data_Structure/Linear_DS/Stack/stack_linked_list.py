
# ============================= Stack using Linked lists ====================================
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self):
        data = int(input("Enter your element: "))
        n = Node(data)
        n.next = self.head
        self.head = n 
        temp = self.head
        print(temp.data,"is on TOP of stack")
    
    def pop(self):
        temp = self.head
        self.head = temp.next
    
    def display(self):
        if self.head is None:
            print("Stack is Empty")
        else:
            print(self.head.data,"is on TOP of stack")
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next

# MAIN 

s = Stack()

while(1):
    print("Enter the options from below:\n1-PUSH Opretaion\n2-POP Opretaion\n3-Display Opretaion\nEnter any key to EXIT Program")
    choice = int(input())
    if choice == 1:
        print("========== PUSH OPERATION ==========")
        s.push()
        print()
    elif choice == 2:
        print("========== POP OPERATION ==========")
        s.pop()
        print()
    elif choice == 3:
        print("========== DISPLAY OPERATION ==========")
        s.display()
        print()
    else:
        print("========== EXIT PROGRAM ==========")
        print()
        break