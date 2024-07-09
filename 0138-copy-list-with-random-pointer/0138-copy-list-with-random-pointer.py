"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        res={}
        curr=head
        while curr:
            new=Node(curr.val)
            res[curr]=new
            curr=curr.next

        curr=head
        while curr:
            temp=res[curr]
            temp.next=res.get(curr.next)
            temp.random=res.get(curr.random)
            curr=curr.next
        
        return res[head]