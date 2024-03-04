# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count(root,MAX,ans):
            if not root:
                return ans
            if root.val>=MAX:
                ans+=1
                MAX=max(root.val,MAX)
            ans = count(root.left,MAX,ans)
            ans = count(root.right,MAX,ans)
            return ans
        ans=0
        ans = count(root,float('-inf'),ans)
        return ans