# ======================= Queue (FIFO) using Lists ========================= 
def enqueue():
    n = int(input("Enter your element: "))
    queue.append(n)
    print(n, "is been added in a queue")

def dequeue():
    if len(queue) == 0:
        print("***********Queue is Empty************")
    else:
        del queue[0] #pop(0)

def display():
    if len(queue) == 0:
        print("***********Queue is Empty************")
    else:
        print("The is Queue is")
        for el in queue:
            print(el,end=" ")

queue = list()

while(1):
    print("Enter your option from the below:\n1-Enqueue Operation\n2-Dequeue Operation\n3-Display Operation\n4-Exit Operation")
    option = int(input())
    if option == 1:
        print("ENQUEUE OPERATION")
        enqueue()
        print()
    elif option == 2:
        print("DEQUEUE OPERATION")
        dequeue()
        print()
    elif option == 3:
        print("DISPLAY OPERATION")
        display()
        print()
    else:
        print("EXIT OPERATION")
        break