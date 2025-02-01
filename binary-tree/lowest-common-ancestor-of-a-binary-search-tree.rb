# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

def dfs(node, target_node, res)
    return if node.nil?
    if node.val == target_node.val
        res.append(node)
        return res
    end
    if dfs(node.left, target_node, res)
        res.append(node)
        return res
    end
    if dfs(node.right, target_node, res)
        res.append(node)
        return res
    end
end

def get_path(root, target_node)
    res = []
    dfs(root, target_node, res)
    res
end

# @param {TreeNode} root
# @param {TreeNode} p
# @param {TreeNode} q
# @return {TreeNode}
def lowest_common_ancestor(root, p, q)
    p_set = Set.new(get_path(root, p))
    q_path = get_path(root, q)
    q_path.each do |node|
        if p_set.include? node
            return node
        end
    end
end