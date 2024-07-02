class MinStack:

    def __init__(self):
        self.vals = []
        self.count = -1
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.count += 1
        self.vals.append(val)
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        if self.count >= 0:
            temp = self.vals.pop()
            self.count -= 1
            if temp == self.min:
                self.min = min(self.vals) if self.count >= 0 else float('inf')

    def top(self) -> int:
        if self.count >= 0:
            return self.vals[-1]
        else:
            raise IndexError("Stack is empty")

    def getMin(self) -> int:
        if self.count >= 0:
            return self.min
        else:
            raise IndexError("Stack is empty")


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
