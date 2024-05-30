"""
Title: 2095. Delete the Middle Node of a Linked List
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        # Edge case: If the list has only one node, return None
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        # Move fast pointer twice as fast as slow pointer
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node
        if prev:
            prev.next = slow.next

        return head

# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    print(result)

# Example usage:
solution = Solution()

# Test case 1
head = create_linked_list([1, 3, 4, 7, 1, 2, 6])
new_head = solution.deleteMiddle(head)
print_linked_list(new_head)  # Output: [1, 3, 4, 1, 2, 6]

# Test case 2
head = create_linked_list([1, 2, 3, 4])
new_head = solution.deleteMiddle(head)
print_linked_list(new_head)  # Output: [1, 2, 4]

# Test case 3
head = create_linked_list([2, 1])
new_head = solution.deleteMiddle(head)
print_linked_list(new_head)  # Output: [2]
