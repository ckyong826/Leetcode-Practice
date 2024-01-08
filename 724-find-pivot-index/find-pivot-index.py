class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left=0
        right=sum(nums)
        for pivot,num in enumerate(nums):
            right-=num
            if left==right:
                return pivot
            left+=num
        return -1