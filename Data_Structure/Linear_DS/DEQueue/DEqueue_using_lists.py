# ================ DEQueue using lists ===================


def enqueueR(data):
    print("Inserting data to Rear:",data)
    print()
    q.append(data)

def enqueueF(data):
    print("\nInserting data form Front:",data)
    print()
    # add at 0 index and shift all elements to the right 
    q.append(0)
    n = len(q)
    for i in range(n-1,0,-1):
        q[i] = q[i-1]
    
    q[0] = data


def dequeueF():
    if len(q) == 0:
        print("Queue is Empty")
    else:
        print("Deleting data at Front", q[0])
        del q[0]
def dequeueR():
    n = len(q)
    if n == 0:
        print("Queue is Empty")
    else:
        print("Deleting data from Rear", q[n-1])
        del q[n-1]

def display():
    if len(q) == 0:
        print("Queue is Empty")
    else:
        print("==========================")
        print("Queue is")
        for i in range(len(q)):
            print(q[i], end=" ")
        print()


q = list()
enqueueR(10)
enqueueR(20)
enqueueR(30)
display()
enqueueF(40)
enqueueF(50)
display()
dequeueF()
display()
dequeueR()
display()

