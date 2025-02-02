# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end

def get_depth(node)
    return 0 if node.nil?
    return 1 + [get_depth(node.left), get_depth(node.right)].max
end

# @param {TreeNode} root
# @return {Integer}
def diameter_of_binary_tree(root)
    return 0 if root.nil?
    left = get_depth(root.left)
    right = get_depth(root.right)
    res = left + right
    [res, diameter_of_binary_tree(root.left), diameter_of_binary_tree(root.right)].max
end