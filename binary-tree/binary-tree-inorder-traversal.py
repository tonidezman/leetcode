# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self, root: Optional[TreeNode], res: List[int]) -> None:
        if root is None:
            return
        self.rec(root.left, res)
        res.append(root.val)
        self.rec(root.right, res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.rec(root, res)
        return res