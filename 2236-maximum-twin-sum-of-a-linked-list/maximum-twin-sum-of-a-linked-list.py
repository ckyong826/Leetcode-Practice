# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp=[]
        slow=head
        temp.append(slow.val)
        fast=head.next
        if fast.next==None:
            return slow.val+fast.val
        while fast and fast.next:
            slow=slow.next
            temp.append(slow.val)
            fast=fast.next.next
        slow=slow.next
        maxSum=temp.pop()+slow.val
        while slow and slow.next:
            slow=slow.next
            maxSum=max(maxSum,temp.pop()+slow.val)
        return maxSum
        
