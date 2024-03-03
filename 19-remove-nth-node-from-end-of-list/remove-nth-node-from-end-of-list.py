# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        curr=head
        while curr:
            l+=1
            curr=curr.next
        l=l-n
        prev=None
        temp=head
        for i in range(l):
            prev=temp
            temp=temp.next
        if l==0:
            head=head.next
        else:
            prev.next=temp.next
        return head

        


                