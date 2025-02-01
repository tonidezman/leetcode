# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end

def get_max_height(node)
    return -Float::INFINITY if node.nil?
    is_leaf = node.left.nil? && node.right.nil?
    return 1 if is_leaf
    left_height = get_max_height(node.left)
    right_height = get_max_height(node.right)
    return 1 + [left_height, right_height].max
end

def get_min_height(node)
    return Float::INFINITY if node.nil?
    is_leaf = node.left.nil? && node.right.nil?
    return 1 if is_leaf
    left_height = get_min_height(node.left)
    right_height = get_min_height(node.right)
    return 1 + [left_height, right_height].min
end

# @param {TreeNode} root
# @return {Boolean}
def is_balanced(root)
    return true if root.nil?
    (get_max_height(root) - get_min_height(root)).abs <= 1
end