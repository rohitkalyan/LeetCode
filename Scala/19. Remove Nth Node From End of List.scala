/**
 * Definition for singly-linked list.
 * class ListNode(_x: Int = 0, _next: ListNode = null) {
 *   var next: ListNode = _next
 *   var x: Int = _x
 * }
 */
object Solution {
    def removeNthFromEnd(head: ListNode, n: Int): ListNode = {
        
 var currentNode = head

    var backRefNode = head
    var backRefNodePos = -n - 1

    while (currentNode != null) {
      if (backRefNodePos >= 0) {
        backRefNode = backRefNode.next
      }

      backRefNodePos += 1
      currentNode = currentNode.next
    }

    if (backRefNodePos == -1)
      head.next
    else {
      if (backRefNode.next != null) {
        backRefNode.next = backRefNode.next.next
      }
      head
    }
  }
}
