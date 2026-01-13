from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def maximumTwinSumOfaLL(self, head: Optional[ListNode]) -> int:
        def findMiddle(head):
            slow = head
            fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow
        
        curr = head
        curr = findMiddle(curr)

        print(curr.val)

        prev = None
        #Reversal
        while curr:
            next_node = curr.next 
            curr.next = prev
            prev = curr
            curr = next_node
        return head

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

def arrToList(arr, n):
    root = None
    for i in range(n - 1, -1, -1):
        root = insert(root, arr[i])

    return root 
if __name__ == '__main__':
    arr = [1,2,3,4,5]
    n = len(arr)
    print("Original List")
    root = arrToList(arr, n)
    display(root)

    print("Revised List")
    sol = Solution()
    root = sol.maximumTwinSumOfaLL(root)
    display(root)