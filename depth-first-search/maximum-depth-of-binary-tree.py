# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return get_length(root)

def get_length(node, res = 0):
    if node is None:
        return res
    return 1 + max(get_length(node.left), get_length(node.right))