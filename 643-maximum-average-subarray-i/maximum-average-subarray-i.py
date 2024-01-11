class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans=sum(nums[:k])
        SUM=ans
        for i in range(len(nums)-k):
            SUM=SUM-nums[i]+nums[i+k]
            ans=max(ans,SUM)
        return ans/k