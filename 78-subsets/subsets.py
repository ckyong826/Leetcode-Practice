class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def helper(temp,start):
            res.append(temp[:])
            for i in range(start,len(nums)):
                temp.append(nums[i])
                helper(temp,i+1)
                temp.pop()
        helper([],0)
        return res
