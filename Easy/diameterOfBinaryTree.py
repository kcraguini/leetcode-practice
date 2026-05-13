from typing import Optional

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diamterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if root.left is None:
            return 1 + self.diamterOfBinaryTree(root.right)
        elif root.right is None:
            return 1 + self.diamterOfBinaryTree(root.left)
        return 1 + max(self.diamterOfBinaryTree(root.left), self.diamterOfBinaryTree(root.right))
    

four = TreeNode(4, None, None)
five = TreeNode(5, None, None)
two = TreeNode(2, four, five)
three = TreeNode(3, None, None)
one = TreeNode(1, two, three) 