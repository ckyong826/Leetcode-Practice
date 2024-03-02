# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        list1,list2=[],[]
        self.findLeaf(root1,list1)
        self.findLeaf(root2,list2)
        return list1 == list2

    def findLeaf(self, root: Optional[TreeNode], temp: List[int]) -> List[int]:
        if not root:
            return
        if not root.left and not root.right:
            temp.append(root.val)
        self.findLeaf(root.left,temp)
        self.findLeaf(root.right,temp)
        return temp
        
