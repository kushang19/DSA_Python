# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Helper function to calculate height of a tree
    def height(self, root):
        # Base case: if root is null, height is 0
        if root is None:
            return 0
        # Height = 1 + max height of left and right subtrees
        return 1 + max(self.height(root.left), self.height(root.right))

    # Function to check if the tree is balanced
    def isBalanced(self, root):
        # Base case: an empty tree is balanced
        if root is None:
            return True

        # Find the height of left and right subtrees
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        # Check if current node is balanced
        if abs(leftHeight - rightHeight) > 1:
            return False

        # Recursively check if left and right subtrees are balanced
        return self.isBalanced(root.left) and self.isBalanced(root.right)


# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)
    root.left.right.right.right = TreeNode(7)

    # Creating an instance of the Solution class
    solution = Solution()

    # Checking if the tree is balanced
    if solution.isBalanced(root):
        print("The tree is balanced.")
    else:
        print("The tree is not balanced.")
