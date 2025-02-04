# Definition for a Node.
# class Node
#     attr_accessor :val, :neighbors
#     def initialize(val = 0, neighbors = nil)
#		  @val = val
#		  neighbors = [] if neighbors.nil?
#         @neighbors = neighbors
#     end
# end

# @param {Node} node
# @return {Node}
def cloneGraph(node)

    hsh = {}
    def dfs(node, hsh)
        return hsh[node] if hsh.include?(node)
        clone = Node.new(node.val)
        hsh[node] = clone
        node.neighbors.each do |neighbor|
            clone.neighbors << dfs(neighbor, hsh)
        end
        clone
    end

    node ? dfs(node, hsh) : nil
end