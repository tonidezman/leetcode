# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return isValid(root, float('-inf'), float('inf'))

def isValid(node: Optional[TreeNode], leftBound: float, rightBound: float) -> bool:
    if node is None:
        return True
    if node.val <= leftBound or node.val >= rightBound:
        return False
    return isValid(node.left, leftBound, node.val) and isValid(node.right, node.val, rightBound)