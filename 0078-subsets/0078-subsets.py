class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def helper(temp,start):
            res.append(temp[:])
            for i in range(start,len(nums)):
                helper(temp+[nums[i]],i+1)
        helper([],0)
        return res
