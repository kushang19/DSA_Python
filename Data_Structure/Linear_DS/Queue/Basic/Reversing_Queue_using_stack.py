queue = [5, 10, 15, 20, 25]
stack = []

# Step 1: Dequeue from queue and push into stack
while len(queue) != 0:
    element = queue[0]      # front of queue
    queue = queue[1:]       # dequeue
    stack.append(element)   # push to stack

# Step 2: Pop from stack and enqueue back to queue
while len(stack) != 0:
    element = stack.pop()   # pop from stack
    queue.append(element)  # enqueue

print(queue)
