class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root) -> int:
    if not root:
        return 0
    if root.left is None:
        return 1 + minDepth(root.right)
    if root.right is None:
        return 1 + minDepth(root.left)
    return 1 + min(minDepth(root.left), minDepth(root.right))

def recursion(root:TreeNode):
    if not root:
        print("null")
        return 
    
    print(root.val)
    left = recursion(root.left)
    right = recursion(root.right)

fifteen = TreeNode(15, None, None)
seven = TreeNode(7, None, None)
nine = TreeNode(9, None, None)
twenty = TreeNode(20, fifteen, seven)
root = TreeNode(3, nine, twenty)

print(f"Minimum depth: {minDepth(root)}")
recursion(root)

