class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num=list(set(nums))
        num.sort()
        nums.clear()
        for i in num:
            nums.append(i)
        return len(nums)
