class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)-2): 
            l = i + 1
            r = len(nums)-1 
            while l < r:
                find = nums[i] + nums[l] + nums[r]
                if find == 0 :
                    res.add(( nums[i] , nums[l] , nums[r]))
                    l += 1
                    r -= 1
                elif find < 0 :
                    l += 1
                else :
                    r -= 1
        return [list(tuplet) for tuplet in res]

           