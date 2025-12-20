from typing import Optional
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow.next
            fast.next.next

            if fast == slow:
                return True
        
        return False

sol = Solution()

#create a linked list with a cycle for testing
one = ListNode(1)
two = ListNode(2)
one.next = two
two.next = one

print(one.next.val)

print(sol.hasCycle(one))