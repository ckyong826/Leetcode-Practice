# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1,res2=[],[]
        def insertTree(root,res):
            if root is None:
                res.append(None)
                return
            res.append(root.val)
            insertTree(root.left,res)
            insertTree(root.right,res)
        insertTree(p,res1)
        insertTree(q,res2)
        return res1==res2