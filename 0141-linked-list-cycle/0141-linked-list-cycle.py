# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        MAP=Counter()
        curr=head
        while curr:
            MAP[curr]+=1
            if MAP[curr]==2:
                return True
            curr=curr.next
        return False