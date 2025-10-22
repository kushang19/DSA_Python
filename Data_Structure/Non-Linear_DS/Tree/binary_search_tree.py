class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        
        if self.key == data:
            return 
        
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    
    def search(self, data):
        if self.key == data:
            print("Node is Found!")
            return 
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is Not present in Tree")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is Not present in Tree")
    
    def preorder(self): # root --> left --> right
        print(self.key, end=" ")
        
        if self.lchild:
            self.lchild.preorder()
        
        if self.rchild:
            self.rchild.preorder()

    def inorder(self): # left --> root -->  right (we get Nodes in sorted order)
        if self.lchild:
            self.lchild.inorder()

        print(self.key, end=" ")
        
        if self.rchild:
            self.rchild.inorder()

    def postorder(self): # left --> right --> root
        if self.lchild:
            self.lchild.postorder()
        
        if self.rchild:
            self.rchild.postorder()
        
        print(self.key, end=" ")

    
    def delete(self,data):
        if self.key is None:
            print("Tree is Empty!")
            return
        
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("Given Node is not Present in the Tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Given Node is not Present in the Tree")
        else:
            if self.lchild is None: # handles case for 0 and 1 child
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None: # handles case for 0 and 1 child
                temp = self.lchild
                self = None
                return temp
            # handles case for 2 child
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        
        return self
            

# case_1
# root = BST(Non )

# case_2
root = BST(10)
# list_1 = [20,4,30,4,1,5,6]
list_1 = [6,3,1,6,98,3,7]
for i in list_1:
    root.insert(i)

root.search(12)
print("Pre-Order")
root.preorder()
print("\n======================")
print("In-Order")
root.inorder()
print("\n======================")
print("Post-Order")
root.postorder()
print("\n======================")
root.delete(6)
print("after delete")
root.preorder()

