class MinStack:

    def __init__(self):
        self.vals=[]
        self.count=-1

    def push(self, val: int) -> None:
        self.count+=1
        self.vals.append(val)

    def pop(self) -> None:
        self.vals.pop()
        self.count-=1

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return min(self.vals)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()