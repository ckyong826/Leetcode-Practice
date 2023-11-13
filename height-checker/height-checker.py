class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = heights[:]
        sorted = True
        indices=0
        while sorted:
            sorted=False
            for i in range(len(temp)-1):
                if(temp[i+1]<temp[i]):
                    temp[i+1],temp[i]=temp[i],temp[i+1]
                    sorted = True
        for i in range(len(heights)):
            if temp[i]!=heights[i]:
                indices+=1
        return indices