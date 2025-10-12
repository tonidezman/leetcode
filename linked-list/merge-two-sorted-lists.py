# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        curr = dummy
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next  
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next  
            curr = curr.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return dummy.next