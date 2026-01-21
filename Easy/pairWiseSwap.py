class Listnode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def pairwiseSwap(self, head):
        curr = head

        while curr and curr.next:
            curr.val, curr.next.val = curr.next.val, curr.val

            curr = curr.next.next


def display(head):

    while head: 
        print(head.val, end=" ")
        head = head.next

    print()


def insert(root, val):
    temp = Listnode(0)

    temp.next = root
    temp.val = val
    root = temp

    return root

def arrToLL(arr, n):
    root = None
    for i in range(n - 1, -1, -1):
        root = insert(root, arr[i])

    return root
        
if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8]
    n = len(arr)
    print("Original Linked List")
    root = arrToLL(arr, n)
    display(root)

    print("After pairwise swap")
    sol = Solution()
    sol.pairwiseSwap(root)
    display(root)