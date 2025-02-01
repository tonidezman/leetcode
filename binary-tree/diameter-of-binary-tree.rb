# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end

def get_length(node, curr=0)
    return curr if node.nil?
    is_leaf = node.left.nil? && node.right.nil?
    return 1 if is_leaf
    left = get_length(node.left, curr)
    right = get_length(node.right, curr)
    return 1 + [left, right].max
end

# @param {TreeNode} root
# @return {Integer}
def diameter_of_binary_tree(root, res=0)
    return 0 if root.nil?
    left = get_length(root.left)
    right = get_length(root.right)
    res = [res, left+right].max
    diameter_of_binary_tree(root.left, res)
    diameter_of_binary_tree(root.right, res)
    res
end
