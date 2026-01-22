from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # two pointers the left pointer would find the given left number and the right pointer would find the right given number
        
        # switch the two val with each other
        
        def swap(left, right):
            left.val, right.val = right.val, left.val    
            print(f"New Swap: L {left.val} R {right.val}")
            return 
        
        Pointer = head 
        
        if head.next is None:
            return head
        
        cnt = 1
        while Pointer:
            if cnt == left:
                tempLeft = Pointer
                
            if cnt == right:
                while True:       
                    swap(tempLeft, Pointer)
                    tempLeft.next
            
            cnt += 1 
            Pointer = Pointer.next
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
    arr = [1,2,3,4,5]
    n = len(arr)

    root = arrToLL(arr, n)
    print("Original LL")
    display(root)

    print("Reversing between 2 and 4")
    sol = Solution()
    root = sol.reverseBetween(root, 2, 4)
    display(root)