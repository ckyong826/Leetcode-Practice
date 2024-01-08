class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea=min(height[0],height[1])*1
        i,j=0,len(height)-1
        while i<j:
            w=j-i
            h=min(height[i],height[j])
            maxArea=max(maxArea,h*w)
            if height[i] <height[j]:
                i+=1
            else:
                j-=1
        return maxArea
                

            