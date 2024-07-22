class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        toD = lambda x,y : math.sqrt(pow((x-0),2)+pow(y-0,2))
        heap = [(toD(x,y),[x,y]) for x,y in points] 
        heapq.heapify(heap)
        res=[heapq.heappop(heap)[1] for n in range(k)]
        return res