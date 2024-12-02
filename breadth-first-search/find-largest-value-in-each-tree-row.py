from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = deque([(root, 0)])
        res = {}
        while queue:
            node, level = queue.popleft()
            if level not in res:
                res[level] = node.val
            else:
                res[level] = max(res[level], node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return res.values()