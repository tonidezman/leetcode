# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end

def generate(nums, lo:, hi:)
    return if lo > hi
    mid = lo + (hi - lo) / 2
    root = TreeNode.new(nums[mid])
    root.left = generate(nums, lo: lo, hi: mid-1)
    root.right = generate(nums, lo: mid+1, hi: hi)
    root
end

# @param {Integer[]} nums
# @return {TreeNode}
def sorted_array_to_bst(nums)
    generate(nums, lo: 0, hi: nums.size-1)
end