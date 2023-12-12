class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i,j=nums[0],nums[1]
        return (i-1)*(j-1)