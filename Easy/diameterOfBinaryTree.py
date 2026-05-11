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
    

