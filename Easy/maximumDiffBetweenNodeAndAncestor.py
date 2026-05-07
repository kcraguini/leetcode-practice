from typing import Optional

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        

        return    
    def preOrder(self, root: Optional[TreeNode]):
        if not root:
            print("null")
            return 

        print(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)


four = TreeNode(4, None, None)
seven = TreeNode(7, None, None)
thirteen = TreeNode(13, None, None)
one = TreeNode(1, None, None)
six = TreeNode(6, four, seven)
fourteen = TreeNode(14, thirteen, None)
three = TreeNode(3, one, six)
ten = TreeNode(10, None, fourteen)
eight = TreeNode(8, three, ten)

sol = Solution()
print(sol.preOrder(eight))