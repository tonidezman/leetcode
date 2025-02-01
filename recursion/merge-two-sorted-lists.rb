# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} list1
# @param {ListNode} list2
# @return {ListNode}
def merge_two_lists(list1, list2)
    dummy = ListNode.new("dummy")
    curr = dummy
    while list1 && list2
        if list1.val < list2.val
            curr.next = list1
            list1 = list1.next
        else
            curr.next = list2
            list2 = list2.next
        end
        curr = curr.next
    end
    if list1
        curr.next = list1
    end
    if list2
        curr.next = list2
    end
    dummy.next
end