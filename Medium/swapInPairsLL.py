from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
        
class Solution:
    def swapPairs(self, head: Node) -> Node:
        
        if not head or not head.next:
            return head

        dummy = head.next               
        prev = None                     
        while head and head.next:
            if prev:
                prev.next = head.next  
            prev = head                 

            next_node = head.next.next  
            head.next.next = head      

            head.next = next_node       
            head = next_node            

        return dummy
                    
        
    
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
    print("After swapping the pairs", end=" ")
    head = sol.swapPairs(root)
    display(head)
