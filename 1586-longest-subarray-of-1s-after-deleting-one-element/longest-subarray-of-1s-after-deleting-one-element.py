class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans,cnt,prev=0,0,-1
        for i in range(n):
            if nums[i]==0:
                ans=max(ans,cnt)
                cnt=i-prev-1
                prev=i
            else:
                cnt+=1
        ans=max(cnt,ans)
        return ans-1 if ans==n else ans

