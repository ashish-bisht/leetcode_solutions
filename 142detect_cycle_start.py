# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head

        while fast:
            fast = fast.next
            if not fast:
                return None
            slow = slow.next
            fast = fast.next

            if slow == fast:
                break

        if not fast:
            return None

        while slow != head:
            slow = slow.next
            head = head.next
        return slow
