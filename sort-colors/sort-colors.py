class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            minIndex=i
            for j in range(i+1,len(nums)):
                if (nums[minIndex]>nums[j]):
                    minIndex=j
            nums[minIndex],nums[i]=nums[i],nums[minIndex]
                