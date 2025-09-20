# ========== Queue Implementation Using One Stack and Recursion =============

#  A queue can be implemented using one stack and recursion. The recursion uses the call stack to temporarily hold elements while accessing the bottom element of the stack, which represents the front of the queue.

class Queue:
    def __init__(self):
        self.s = []

    def enqueue(self,x):
        self.s.append(x) 
    
    def size(self):
        return len(self.s)
    
    def front(self):
        if not self.s:
            print("Queue UnderFlow")
            return -1
        
        x = self.s.pop()

        if not self.s:
            self.s.append(x)
            return x
        
        item = self.front()

        self.s.append(x)
        return item
    
    def dequeue(self):
        if not self.s:
            print("Queue UnderFlow")
            return -1
        
        x = self.s.pop()

        if not self.s:
            return x 
        
        item = self.dequeue()

        self.s.append(x)
        return item


if __name__ == "__main__":
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Front:", q.front()) 
    print("Size:", q.size())

    print("Dequeue:", q.dequeue()) 
    print("Front:", q.front())     
    print("Size:", q.size())     

    print("Dequeue:", q.dequeue()) 
    print("Dequeue:", q.dequeue()) 
    print("Dequeue:", q.dequeue())


