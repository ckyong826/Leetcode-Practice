# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        def findDiam(root):
            if root is None:
                return 0
            left=findDiam(root.left)
            right=findDiam(root.right)
            self.diameter=max(self.diameter,(left+right))
            return max(left,right) +1
        findDiam(root)
        return self.diameter