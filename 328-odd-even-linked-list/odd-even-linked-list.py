# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        temp=head
        counter=1
        length=1
        if(head==None):
            return head
        while(temp.next):
            temp=temp.next
            length+=1
        if(length==2):
            return head
        for i in range(length):
            if(counter%2==0):
                prev.next=curr.next
                temp.next=curr
                temp=temp.next
                temp.next=None
                curr=prev.next
                counter+=1
            else:
                prev=curr
                curr=curr.next
                counter+=1
        return head