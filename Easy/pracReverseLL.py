class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverse_list(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
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
    root = arrToList(arr, n)
    display(root)

    sol = Solution()
    print("After being reversed")
    root = sol.reverse_list(root)
    display(root)
