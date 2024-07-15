class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        MIN=nums[0]
        while l<r:
            mid=(l+r)//2
            MIN=min(MIN,nums[mid])
            if nums[mid] > nums[r]:
                l=mid+1
                MIN=min(MIN,nums[l])
            else:
                r=mid
        return MIN
        