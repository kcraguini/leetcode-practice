class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for parent, child, isLeft in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent, None, None)
            if child not in nodes:
                nodes[child] = TreeNode(child, None, None)

            if isLeft:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

            children.add(child)

        for node in nodes.values():
            if node.val not in children:
                return node
            

s = Solution()
print(s.createBinaryTree([[1,2,1],[1,3,0],[2,4,1]]))
print(s.createBinaryTree([[1,2,1],[2,3,0],[3,4,1]]))