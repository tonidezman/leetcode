# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end

def get_height(node)
    return 0 if node.nil?
    return 1 + [get_height(node.left), get_height(node.right)].max
end

# @param {TreeNode} root
# @return {Boolean}
def is_balanced(root)
    return true if root.nil?
    left = get_height(root.left)
    right = get_height(root.right)
    return false if (right - left).abs > 1
    return is_balanced(root.left) && is_balanced(root.right)
end
