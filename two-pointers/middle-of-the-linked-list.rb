# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @return {ListNode}
def middle_node(head)
    return if head.nil?
    fast = slow = head
    while fast
        fast = fast.next
        if fast
            fast = fast.next
            slow = slow.next
        end
    end
    slow
end