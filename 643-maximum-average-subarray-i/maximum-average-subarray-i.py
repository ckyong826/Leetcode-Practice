class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans=sum(nums[:k])
        SUM=ans
        for i in range(1,len(nums)-k+1):
            SUM=SUM-nums[i-1]+nums[i+k-1]
            ans=max(ans,SUM)
        return ans/k