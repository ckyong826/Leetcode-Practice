# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.p,self.i=0,0
        def build(stop):
            if len(inorder)>self.i and inorder[self.i]!=stop:
                root=TreeNode(preorder[self.p])
                self.p+=1
                root.left=build(root.val)
                self.i+=1
                root.right=build(stop)
                return root
            return None
        return build(None)