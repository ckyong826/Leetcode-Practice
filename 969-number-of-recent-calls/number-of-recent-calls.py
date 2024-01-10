class RecentCounter:

    def __init__(self):
        self.count=[]

    def ping(self, t: int) -> int:
        temp=self.count
        temp.append(t)
        r=[t-3000,t]
        while temp[0]<r[0] or temp[0]>r[1]:
            temp.pop(0)
        return len(temp)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)