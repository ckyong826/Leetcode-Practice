# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:return head 
        if head.next==None: return None
        prev=None
        fast=head
        slow=head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        if slow:
            prev.next=slow.next
        else:
            prev.next=None
        return head