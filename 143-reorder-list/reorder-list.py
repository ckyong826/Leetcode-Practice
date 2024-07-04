# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid,right=head,head
        while right and right.next:
            mid=mid.next
            right=right.next.next
        prev=None
        rev=mid
        while rev:
            temp=rev.next
            rev.next=prev
            prev=rev
            rev=temp
        first=head
        second=prev
        while second.next:
            tmp1,tmp2=first.next,second.next
            first.next=second
            second.next=tmp1
            first=tmp1
            second=tmp2
        return head
        
                
