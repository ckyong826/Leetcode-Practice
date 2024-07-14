# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def InOrder(root):
            if not root:
                return []
            return InOrder(root.left) + [root.val] + InOrder(root.right)
        res=InOrder(root)
        return res[k-1] 