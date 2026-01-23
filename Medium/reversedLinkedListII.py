from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move prev to the node just before the left position
        for _ in range(left - 1):
            prev = prev.next
        
        # Start reversing from the left position
        curr = prev.next
        
        # Reverse the sublist between left and right
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        
        return dummy.next

def insert(root, val):
    temp = ListNode(0)
    temp.val = val
    temp.next = root
    root = temp
    return root

def display(root):
    while root:
        print(root.val, end=" ")
        root = root.next
    print()

def arrToLL(arr, n):
    root = None
    for i in range(n - 1, -1, -1):
        root = insert(root, arr[i])
    return root

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    n = len(arr)

    root = arrToLL(arr, n)
    print("Original LL")
    display(root)

    print("Reversing between 2 and 5")
    sol = Solution()
    root = sol.reverseBetween(root, 2, 8)
    display(root)