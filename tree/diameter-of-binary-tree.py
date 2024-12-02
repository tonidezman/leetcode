# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        res = 0
        left = get_length(root.left)
        right = get_length(root.right)
        curr = left + right
        return max(curr, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

def get_length(node, res=0):
    if node is None:
        return 0
    return 1 + max(get_length(node.left), get_length(node.right))
