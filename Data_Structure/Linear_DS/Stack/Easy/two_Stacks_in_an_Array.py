# ============== Implement two Stacks in an Array ==================

# Create a data structure twoStacks that represent two stacks. Implementation of twoStacks should use only one array, i.e., both stacks should use the same array for storing elements. 

# Following functions must be supported by twoStacks.

# push1(int x) --> pushes x to first stack 
# push2(int x) --> pushes x to second stack
# pop1() --> pops an element from first stack and return the popped element 
# pop2() --> pops an element from second stack and return the popped element

# Input: push1(1), push2(2), pop1(), push1(3), pop1(), pop1()
# Output: [1, 3, -1]
# Explanation: push1(1) the stack1 will be [1]
# push2(2) the stack2 will be [2]
# pop1() the popped element will be 1 
# push1(3) the stack1 will be [3]
# pop1() the popped element will be 3
# pop1() the stack1 is now empty hence returned -1

class TwoStack:
    def __init__(self,n):
        self.size = n
        self.arr = [0] * n
        self.top1 = -1
        self.top2 = n

    def push1(self,x):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = x
    
    def push2(self, x):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = x
    
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        return -1
    
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        return -1


if __name__ == "__main__":
    ts = TwoStack(5)
    print(ts.arr)

    ts.push1(2)
    ts.push1(3)
    ts.push2(4)
    print(ts.arr)

    print(ts.pop1(), end=' ')  
    print(ts.pop2(), end=' ')  
    print(ts.pop2(), end=' ') 




    # Input: push1(1), push2(2), pop1(), push1(3), pop1(), pop1()
    # Output: [1, 3, -1]

    # ts.push1(1)
    # ts.push2(2)
    # print(ts.pop1(), end=' ')  
    # ts.push1(3)

    # print(ts.pop1(), end=' ')  
    # print(ts.pop1(), end=' ') 




 