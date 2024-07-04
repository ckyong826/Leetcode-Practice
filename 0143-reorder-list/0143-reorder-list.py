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
        queue=collections.deque()
        curr=head.next

        while curr:
            queue.append(curr)
            curr=curr.next
        
        curr=head
        while len(queue)>1:
            curr.next=queue.pop()
            curr=curr.next
            curr.next=queue.popleft()
            curr=curr.next
        
        if queue:
            curr.next=queue.pop()
            curr=curr.next
        
        curr.next=None
        return head
                
