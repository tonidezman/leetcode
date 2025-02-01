# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @return {Boolean}
def hasCycle(head)
    return false if head.nil?

    slow = fast = head
    while fast
        fast = fast.next
        return true if fast == slow
        if fast
            fast = fast.next
            slow = slow.next
        end
    end
    false
end