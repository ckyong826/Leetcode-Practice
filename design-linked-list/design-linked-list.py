class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class MyLinkedList:

    def __init__(self):
        self.head=None

    def get(self, index: int) -> int:
        curr=self.head
        for i in range(index):
            if curr is None:
                return -1
            curr=curr.next
        return curr.val if curr else -1

    def addAtHead(self, val: int) -> None:
        temp=Node(val)
        temp.next=self.head
        self.head=temp

    def addAtTail(self, val: int) -> None:
        temp = Node(val)
        if not self.head:
            self.head = temp
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = temp

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        curr = self.head
        temp = Node(val)
        for i in range(index - 1):
            if curr is None:
                return
            curr = curr.next
        if not curr:
            return
        temp.next = curr.next
        curr.next = temp

    def deleteAtIndex(self, index: int) -> None:
        if index <0:
            return
        if index == 0:
            if self.head:
                self.head=self.head.next
            return
        curr=self.head
        for i in range(index-1):
            if curr is None or curr.next is None:
                return
            curr=curr.next
        if curr.next:
            curr.next=curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)