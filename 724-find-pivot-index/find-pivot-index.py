class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            leftSum,rightSum=0,0
            leftSum=sum(nums[:i])
            rightSum=sum(nums[i+1:])
            if leftSum==rightSum:
                return i
        return -1