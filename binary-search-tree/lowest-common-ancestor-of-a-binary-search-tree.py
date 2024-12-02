# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_nodes = find_parents(root, p)
        curr = root
        res = curr
        while True:
            if curr.val == q.val:
                if q.val in parent_nodes:
                    return q
                else:
                    return res
            elif curr.val > q.val:
                curr = curr.left
            else:
                curr = curr.right
            if curr.val in parent_nodes:
                res = curr
def find_parents(root, node):
    res = set([root.val])
    while True:
        if root.val == node.val:
            res.add(node.val)
            return res
        elif root.val < node.val:
            root = root.right
        else:
            root = root.left
        res.add(root.val)
    return res