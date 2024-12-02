# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast:
            fast = fast.next
            if fast:
                slow = slow.next
                fast = fast.next
                if fast and fast == slow:
                    return True
        return False
       