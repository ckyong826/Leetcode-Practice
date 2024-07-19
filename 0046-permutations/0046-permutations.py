class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def helper(temp):
            if len(temp)==len(nums):
                res.append(temp[:])
            for i in range(len(nums)):
                if nums[i] not in temp:
                    helper(temp+[nums[i]])
            return res
        return helper([])