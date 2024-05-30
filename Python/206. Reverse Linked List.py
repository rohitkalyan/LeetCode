"""
Title: 206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head

        while current:
            next_node = current.next  # Save the next node
            current.next = prev  # Reverse the current node's pointer
            prev = current  # Move prev to current node
            current = next_node  # Move to the next node

        return prev  # prev will be the new head at the end


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
head = create_linked_list([1, 2, 3, 4, 5])
new_head = solution.reverseList(head)
print_linked_list(new_head)  # Output: [5, 4, 3, 2, 1]

# Test case 2
head = create_linked_list([1, 2])
new_head = solution.reverseList(head)
print_linked_list(new_head)  # Output: [2, 1]

# Test case 3
head = create_linked_list([])
new_head = solution.reverseList(head)
print_linked_list(new_head)  # Output: []
