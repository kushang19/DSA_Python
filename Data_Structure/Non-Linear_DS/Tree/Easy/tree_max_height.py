# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        # Base case: if the node is null, return 0
        if root is None:
            return 0
        # Recursively find the depth of the left and right subtrees
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # The depth of the tree is 1 current node + the maximum depth of the subtrees
        return 1 + max(left, right)

# Main method to test the function
if __name__ == "__main__":
    solution = Solution()
    # Example usage:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Maximum Depth:", solution.maxDepth(root))
