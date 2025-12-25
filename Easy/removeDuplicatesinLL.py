from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
        
class Solution:
        
    def deleteDuplicates(self, head: Optional[Node]) -> Optional[Node]:
            def delete(prev_node):
                if prev_node and prev_node.next:
                    prev_node.next = prev_node.next.next
            
            current = head
        
            while current and current.next:
                if current.val == current.next.val:
                    delete(current)
                    
                else:
                    current = current.next 
                #display(head)
            
            return head
                    
        
    
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
    arr = [1,1,2,3,3]
    n = len(arr)
    root = arrayToList(arr, n)
    print("Original List:", end=" ")
    display(root)
    
    sol = Solution()
    print("List after removing duplicates:", end=" ")
    head = sol.deleteDuplicates(root)
    display(head)
