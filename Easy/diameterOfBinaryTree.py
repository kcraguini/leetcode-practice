from typing import Optional

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def helper(root):
            if not root:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)
        
        helper(root)
        return self.diameter
    
    
    def preOrder(self, root: Optional[TreeNode]):
        if not root:
            return
        
        print(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)
    

four = TreeNode(4, None, None)
five = TreeNode(5, None, None)
two = TreeNode(2, four, five)
three = TreeNode(3, None, None)
one = TreeNode(1, two, three) 

sol = Solution()
print(sol.diameterOfBinaryTree(one))
#sol.preOrder(one)

otherTwo = TreeNode(2, None, None)
otherOne = TreeNode(1, otherTwo, None)
print(sol.diameterOfBinaryTree(otherOne))
