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
        
        def helper(root, curr_min, curr_max):  
            if not root:
                return abs(curr_max - curr_min)   
            # Need to traverse both
            curr_min = min(curr_min, root.val)
            curr_max = max(curr_max, root.val)

            print(f"This is the min {curr_min}, max {curr_max}")

            return max(helper(root.left, curr_min, curr_max), helper(root.right, curr_min, curr_max)) 

            

        return helper(root, root.val, root.val)

        

        
        

           
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
print(sol.maxAncestorDiff(eight))
#print(sol.preOrder(eight))