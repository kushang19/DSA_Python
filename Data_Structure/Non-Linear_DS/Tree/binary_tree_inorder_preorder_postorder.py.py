class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)
    
    def insert(self, data):
        new_node = Node(data)

        queue = [self.root]

        while len(queue) > 0:
            current = queue.pop(0)

            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)

        
            if current.right is None:
                current.right = new_node
                return 
            else:
                queue.append(current.right)

    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)

    # def preorder(self, node):
    #     if node:
    #         print(node.data, end=" ")
    #         self.preorder(node.left)
    #         self.preorder(node.right)

    # def postorder(self, node):
    #     if node:
    #         self.postorder(node.left)
    #         self.postorder(node.right)
    #         print(node.data, end=" ")

    

tree = BinaryTree(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)

print("Inorder Traversal:")
tree.inorder(tree.root)

# print("\nPreorder Traversal:")
# tree.preorder(tree.root)  # Output: 10 5 3 7 15

# print("\nPostorder Traversal:")
# tree.postorder(tree.root)  # Output: 3 7 5 15 10