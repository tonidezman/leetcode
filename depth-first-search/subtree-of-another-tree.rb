# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end

def same(root, sub_root)
    return true if root.nil? && sub_root.nil?
    return false if root.nil? || sub_root.nil?
    return false if root.val != sub_root.val
    same(root.left, sub_root.left) && same(root.right, sub_root.right)
end

def dfs(root, sub_root)
    return false if root.nil? || sub_root.nil?
    return true if same(root, sub_root)
    dfs(root.left, sub_root) || dfs(root.right, sub_root)
end

# @param {TreeNode} root
# @param {TreeNode} sub_root
# @return {Boolean}
def is_subtree(root, sub_root)
    dfs(root, sub_root)
end