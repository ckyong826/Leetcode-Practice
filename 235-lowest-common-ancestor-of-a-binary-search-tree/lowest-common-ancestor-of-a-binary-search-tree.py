# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        if root.val > p.val and root.val > q.val:
            ans = self.lowestCommonAncestor(root.left,p,q)
        elif root.val < p.val and root.val < q.val:
            ans = self.lowestCommonAncestor(root.right,p,q)
        else:
            ans = root
        return ans
