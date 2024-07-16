class LRUCache:
    class Node:
        def __init__(self,key=None,val=None):
            self.key=key
            self.val=val
            self.prev=None
            self.next=None
    def __init__(self, capacity: int):
        self.cap=capacity
        self.head=self.Node()
        self.tail=self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache={}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        n = self.cache[key]
        self.remove(n)
        self.add(n)
        return n.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        elif len(self.cache) == self.cap:
            if len(self.cache )>0:
                self.cache.pop(self.tail.prev.key)
                self.remove(self.tail.prev)
        n=self.Node(key,value)
        self.add(n)
        self.cache[key] = n
    
    def add(self,node):
        temp=self.head.next
        self.head.next=node
        node.prev=self.head
        node.next=temp
        temp.prev=node

    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)