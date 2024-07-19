class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        def helper(temp,start):
            res.add(tuple(temp))
            for i in range(start,len(nums)):
                helper(temp+[nums[i]],i+1)
            return res
        helper([],0)
        return [list(subset) for subset in res]