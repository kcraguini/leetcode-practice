from typing import Optional
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        
        slow = prev
        if slow and slow.next:
            slow.next = slow.next.next

        return head
    
if __name__ == '__main__':
    sol = Solution()
    
    # Helper function to create a linked list from a list
    def create_linked_list(lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for value in lst[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    # Helper function to print the linked list
    def print_linked_list(head):
        current = head
        values = []
        while current:
            values.append(str(current.val))
            current = current.next
        print("->".join(values))

    # Test cases
    head = create_linked_list([1, 3, 4, 7, 1, 2, 6])
    print("Original list:")
    print_linked_list(head)
    modified_head = sol.deleteMiddle(head)
    print("After deleting middle node:")
    print_linked_list(modified_head)

    head = create_linked_list([1, 2, 3, 4])
    print("\nOriginal list:")
    print_linked_list(head)
    modified_head = sol.deleteMiddle(head)
    print("After deleting middle node:")
    print_linked_list(modified_head)

    head = create_linked_list([2, 1])
    print("\nOriginal list:")
    print_linked_list(head)
    modified_head = sol.deleteMiddle(head)
    print("After deleting middle node:")
    print_linked_list(modified_head)

    head = create_linked_list([1])
    print("\nOriginal list:")
    print_linked_list(head)
    modified_head = sol.deleteMiddle(head)
    print("After deleting middle node:")
    print_linked_list(modified_head)