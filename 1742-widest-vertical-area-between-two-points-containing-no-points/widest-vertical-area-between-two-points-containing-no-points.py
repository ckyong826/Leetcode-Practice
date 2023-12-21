class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        area=0
        for i in range(1,len(points)):
            temp=points[i][0]-points[i-1][0]
            area=max(temp,area)
        return area