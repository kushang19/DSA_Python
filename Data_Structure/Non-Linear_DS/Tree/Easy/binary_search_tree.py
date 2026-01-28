class BST:
    def __init__(self,root_data):
        self.root = root_data
        self.left = None
        self.right = None
    
    def insert(self,data):
        if self.root is None:
            self.root = data
            return
        
        if self.root == data:
            return 
        
        if self.root > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)

    
    def search(self, data):
        if self.root == data:
            print("Node is Found!")
            return 
        if data < self.root:
            if self.left:
                self.left.search(data)
            else:
                print("Node is Not present in Tree")
        else:
            if self.right:
                self.right.search(data)
            else:
                print("Node is Not present in Tree")
    
    def delete(self,data):
        if self.root is None:
            print("Tree is Empty!")
            return
        
        if data < self.root:
            if self.left:
                self.left = self.left.delete(data)
            else:
                print("Given Node is not Present in the Tree")
        elif data > self.root:
            if self.right:
                self.right = self.right.delete(data)
            else:
                print("Given Node is not Present in the Tree")
        else:
            if self.left is None: # handles case for 0 and 1 child
                temp = self.right
                self = None
                return temp
            if self.right is None: # handles case for 0 and 1 child
                temp = self.left
                self = None
                return temp
            # handles case for 2 child
            node = self.right
            while node.left:
                node = node.left
            self.root = node.root
            self.right = self.right.delete(node.root)
        
        return self
            
    def preorder(self): # root --> left --> right
        print(self.root, end=" ")
        
        if self.left:
            self.left.preorder()
        
        if self.right:
            self.right.preorder()

    def inorder(self): # left --> root -->  right (we get Nodes in sorted order)
        if self.left:
            self.left.inorder()

        print(self.root, end=" ")
        
        if self.right:
            self.right.inorder()

    def postorder(self): # left --> right --> root
        if self.left:
            self.left.postorder()
        
        if self.right:
            self.right.postorder()
        
        print(self.root, end=" ")
    
# case_1
# root = BST(None)

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

