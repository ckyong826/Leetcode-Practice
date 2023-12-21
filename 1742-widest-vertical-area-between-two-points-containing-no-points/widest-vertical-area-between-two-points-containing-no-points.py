class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        area=points[1][0]-points[0][0]
        for i in range(1,len(points)-1):
            temp=points[i+1][0]-points[i][0]
            if temp>area:
                area=temp
        return area