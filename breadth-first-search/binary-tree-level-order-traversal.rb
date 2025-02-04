require 'thread'

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {Integer[][]}
def level_order(root)
    return [] if root.nil?
    res = []
    queue = Queue.new
    queue << [root, 0]
    until queue.empty?
        node, level = queue.pop
        if level == res.size
            res << [node.val]
        else
            res[level] << node.val
        end
        queue << [node.left, level+1] if node.left
        queue << [node.right, level+1] if node.right
    end
    res
end