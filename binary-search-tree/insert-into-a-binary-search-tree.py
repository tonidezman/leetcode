# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        parent = None
        node = root
        while node:
            parent = node
            if val > node.val:
                node = node.right
            else:
                node = node.left
        if val > parent.val:
            parent.right = TreeNode(val)
        else:
            parent.left = TreeNode(val)
        return root