# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head.next
        SUM=0
        prev=None
        temp=head
        while curr:
            if curr.val==0:
                temp.val=SUM
                prev=temp
                temp=temp.next
                SUM=0
            else:
                SUM+=curr.val
            curr=curr.next
        prev.next=None
        return head