# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end

def preorder(root, res)
    return if root.nil?
    res << root.val
    preorder(root.left, res)
    preorder(root.right, res)
end

# @param {TreeNode} root
# @return {Integer[]}
def preorder_traversal(root)
    res = []
    preorder(root, res)
    res
end