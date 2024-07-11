# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def find(root):
            if not root:
                return 0, True
            l,b1=find(root.left)
            r,b2=find(root.right)
            h=max(l,r) + 1
            b=b1 and b2 and abs(l-r)<=1
            return h, b
        _, b = find(root)
        return b