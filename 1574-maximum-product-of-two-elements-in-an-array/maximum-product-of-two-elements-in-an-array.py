class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        i,j=nums[-1],nums[-2]
        return (i-1)*(j-1)