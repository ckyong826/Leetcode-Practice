# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1,c2=l1,l2
        str1,str2="",""
        while c1:
            str1+=str(c1.val)
            c1=c1.next
        while c2:
            str2+=str(c2.val)
            c2=c2.next
        str1=str1[::-1]
        str2=str2[::-1]
        SUM=str(int(str1)+int(str2))
        SUM=SUM[::-1]
        res=ListNode()
        curr=res
        for s in SUM:
            curr.next=ListNode(int(s))
            curr=curr.next
        return res.next