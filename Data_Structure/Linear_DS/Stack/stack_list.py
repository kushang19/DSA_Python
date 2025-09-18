
# ============================= Stack using list ====================================

def push():
    n = int(input("Enter the element to be inserted in stack: "))
    if len(stack) == 0:
        stack.append(n)
    else:
        stack.insert(0,n)

    print(n," is inserted into stack")

def pop():
    if len(stack) == 0:
        print("STACK IS EMPTY")
    else:
        print(stack[0], "is deleted from stack")
        del stack[0] #pop(0)

def display():
    if len(stack) == 0:
        print("STACK IS EMPTY")
    else:
        print("ELEMENTS OF STACK ARE")
        for el in stack:
            print(el)
        print("TOP of the stack is ", stack[0])



# MAIN 
stack = list()
while(1):
    print("Enter the options from below:\n1-PUSH Opretaion\n2-POP Opretaion\n3-Display Opretaion\nEnter any key to EXIT Program")
    str = int(input())
    if str == 1:
        print("PUSH OPERATION")
        push()
        print()
    elif str == 2:
        print("POP OPERATION")
        pop()
        print()
    elif str == 3:
        print("DISPLAY OPERATION")
        display()
        print()
    else:
        print("EXIT PROGRAM")
        print()
        break