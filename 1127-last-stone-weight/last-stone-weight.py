class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-num for num in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            a=heapq.heappop(heap)
            b=heapq.heappop(heap)
            temp=a-b
            heapq.heappush(heap,temp)
        return -heap[0]
