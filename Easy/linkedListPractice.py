from typing import Optional

class ListNode:
    def __init__ (self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def delete(curr):
            if curr and curr.next:
                curr.next = curr.next.next
            return curr
        
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                delete(curr)
            curr = curr.next


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

def arrToLL(arr, n):
    root = None

    for i in range(n - 1, -1, -1):
        root = insert(root, arr[i])

    return root

if __name__ == '__main__':
    arr = [1,1,2,3,3]
    n = len(arr)

    root = arrToLL(arr, n)
    print("Original LL")
    display(root)

    print("Taking out the duplicates")
    sol = Solution()
    root = sol.deleteDuplicates(root)
    
    display(root)