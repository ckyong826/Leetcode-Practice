class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        toD = lambda x,y : math.sqrt(pow((x-0),2)+pow(y-0,2))
        heap = [(toD(x,y),[x,y]) for x,y in points] 
        heapq.heapify(heap)
        res=[]
        for i in range(k):
            a,b = heapq.heappop(heap)
            res.append(b)
        return res