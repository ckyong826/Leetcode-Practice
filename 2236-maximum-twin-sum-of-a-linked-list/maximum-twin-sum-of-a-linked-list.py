# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head
        maxSum=0
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        curr,prev=slow,None
        while curr:
            curr.next,prev,curr=prev,curr,curr.next
        while prev:
            maxSum=max(maxSum,prev.val+head.val)
            prev=prev.next
            head=head.next
        return maxSum
        
