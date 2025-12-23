from typing import Optional

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)

one.next = two
two.next = three
three.next = four
four.next = five

sol = Solution()
pnt = sol.middleNode(one)

print(pnt.val)
