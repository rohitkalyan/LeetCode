"""
Tilte: 2130. Maximum Twin Sum of a Linked List
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: ListNode) -> int:
        if not head or not head.next:
            return 0

        # Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Compute the twin sums and find the maximum twin sum
        max_twin_sum = 0
        first_half = head
        second_half = prev
        while second_half:
            twin_sum = first_half.val + second_half.val
            max_twin_sum = max(max_twin_sum, twin_sum)
            first_half = first_half.next
            second_half = second_half.next

        return max_twin_sum

# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Example usage:
solution = Solution()

# Test case 1
head = create_linked_list([5, 4, 2, 1])
print(solution.pairSum(head))  # Output: 6

# Test case 2
head = create_linked_list([4, 2, 2, 3])
print(solution.pairSum(head))  # Output: 7

# Test case 3
head = create_linked_list([1, 100000])
print(solution.pairSum(head))  # Output: 100001
