class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def show(self):
        if self.left:
            self.left.show()
        print(self.data)
        if self.right:
            self.right.show()


root = Node(100)
root.left = Node(99)
root.right = Node(101)
root.show()