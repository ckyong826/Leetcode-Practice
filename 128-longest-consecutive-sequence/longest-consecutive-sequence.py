class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        count=1
        maxCount=1
        temp=nums[0]
        for i in nums:
            if temp+1 == i:
                count+=1
            elif temp==i:
                pass
            else:
                count=1
            temp=i
            maxCount=max(count,maxCount)
        return maxCount