from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def delete(prev):
            while prev.val == prev.next.val:
                prev.next = prev.next.next
            
        seenVals = set()
        curr = head
        while curr and curr.next:
            if curr.val in seenVals:
                delete(curr)
            else:
                seenVals.add(curr.val)
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

def arrayToList(arr, n):
    root = None
    for i in range(n - 1, -1, -1):
        root = insert(root, arr[i])
    return root

if __name__ == '__main__':
    arr = [1,2,3,3,4,4,5]
    n = len(arr)
    root = arrayToList(arr, n)
    
    #Original
    print("Original Linked List")
    display(root)

    #Revised LL
    sol = Solution()
    root = sol.deleteDuplicates(root)
    print("Revised Linked List")
    display(root)