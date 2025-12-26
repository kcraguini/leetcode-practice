from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
        
class Solution:
        
    def reverse_list(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next # first, make sure we don't lose the next node
            curr.next = prev      # reverse the direction of the pointer
            prev = curr           # set the current node to prev for the next node
            curr = next_node      # move on
            
        return prev
                    
        
    
def insert(root, val):
    temp = Node(0)
    temp.val = val
    temp.next = root
    root = temp
    return root
    
def display(root):
    while(root != None):
        print(root.val, end=" ")
        root = root.next
    print()

def arrayToList(arr, n):
    root = None
    for i in range(n - 1, -1, -1):
        root = insert(root, arr[i])
    return root
    
if __name__ == '__main__':
    arr = [1,2,3,4,5]
    n = len(arr)
    root = arrayToList(arr, n)
    print("Original List:", end=" ")
    display(root)
    
    sol = Solution()
    print("After reversing the list", end=" ")
    head = sol.reverse_list(root)
    display(head)
