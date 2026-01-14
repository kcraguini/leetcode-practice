class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def swa

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

    return root

def arrToList(arr, n):
    root = None
    for i in range(n - 1, -1, -1):
        root = insert(root, arr[i])

    return root

if __name__ == '__main__':
    arr = [1,2,3,4,5,6]
    n = len(arr)
    root = arrToList(arr, n)
    print("Original LL")
    display(root)


    print("Swapped Node")
    sol = Solution()
    root = sol.swapNode(root)
    display(root)
