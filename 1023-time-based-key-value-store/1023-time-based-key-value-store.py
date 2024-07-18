class TimeMap:

    def __init__(self):
        self.h=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.h[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        temp = self.h.get(key,[])
        l,r=0,len(temp)
        ans=""
        while l<r:
            mid = (l+r)//2
            if temp[mid][0] <= timestamp:
                ans= temp[mid][1]
                l=mid+1
            else:
                r=mid
        return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)