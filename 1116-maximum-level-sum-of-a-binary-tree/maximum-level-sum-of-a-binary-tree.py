# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque([root])
        d=defaultdict(int)
        level=1
        while q:
            SUM=0
            for i in range(len(q)):
                node=q.popleft()
                SUM+=node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            d[level] = SUM
            level+=1
        if not d:
            return 0
        ans = max(d,key=d.get)
        return ans
            